import unittest

from hl7apy import load_reference
from hl7apy.parser import parse_message
from hl7apy.validation import VALIDATION_LEVEL, Validator


class TestOBXConditionalFields(unittest.TestCase):
    """
    OBX-2 (Value Type) and OBX-4 (Observation Sub-ID) are conditional (C) in every version
    from 2.3 to 2.8, so an OBX without them is valid. Other versions already define them as optional.
    """

    def test_obx_2_and_4_are_optional(self):
        for version in ('2.3', '2.3.1', '2.4', '2.5', '2.5.1', '2.6', '2.7', '2.8', '2.8.1', '2.8.2'):
            cardinalities = {c[0]: c[2] for c in load_reference('OBX', 'Segment', version)[1]}
            for child in ('OBX_2', 'OBX_4'):
                self.assertEqual(cardinalities[child], (0, 1), '{} in {}'.format(child, version))

    def test_obx_without_sub_id_validates(self):
        for version in ('2.3.1', '2.7', '2.8'):
            msg = (
                'MSH|^~\\&|LAB|HOSP|EHR|HOSP|20260101120000||ORU^R01|1|P|{}\r'
                'PID|1||123||DOE^JOHN||19800101|M\r'
                'OBR|1||555|2345-7^GLUCOSE^LN\r'
                'OBX|1|NM|2345-7^GLUCOSE^LN||95|mg/dL|70-99|N|||F\r'
            ).format(version)
            errors = Validator.validate(parse_message(msg), return_errors=True).errors
            self.assertNotIn('Missing required child OBX.OBX_4', [str(e) for e in errors], version)
            self.assertNotIn('Missing required child OBX.OBX_2', [str(e) for e in errors], version)

    def test_strict_parse_without_sub_id(self):
        msg = (
            'MSH|^~\\&|LAB|HOSP|EHR|HOSP|20260101120000||ORU^R01|1|P|2.3.1\r'
            'PID|1||123||DOE^JOHN||19800101|M\r'
            'OBR|1||555|2345-7^GLUCOSE^LN\r'
            'OBX|1|NM|2345-7^GLUCOSE^LN||95|mg/dL|70-99|N|||F\r'
        )
        parse_message(msg, validation_level=VALIDATION_LEVEL.STRICT, force_validation=True)


if __name__ == '__main__':
    unittest.main()
