# -*- coding: utf-8 -*-
#
# Copyright (c) 2012-2018, CRS4
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from __future__ import absolute_import
import unittest

from datetime import datetime
from hl7apy.base_datatypes import DT, TM, DTM, ST, FT, ID, IS, TX, GTS, NM, SI, TN
from hl7apy.v2_7 import ST as ST27, FT as FT27, ID as ID27, IS as IS27, TX as TX27, GTS as GTS27, SNM
from hl7apy.factories import datatype_factory
from hl7apy.exceptions import InvalidDateFormat, InvalidDateOffset, MaxLengthReached, \
    InvalidHighlightRange, InvalidDataType, InvalidMicrosecondsPrecision
from hl7apy.validation import VALIDATION_LEVEL
from decimal import Decimal


class TestDatatypeFactory(unittest.TestCase):

    def test_datatype_creation(self):
        st = datatype_factory('ST', 'string')
        self.assertEqual(st.classname, 'ST')

    def test_datatype_creation_strict(self):
        tx = datatype_factory('TX', 'text', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertEqual(tx.classname, 'TX')

    def test_invalid_datatype_creation(self):
        self.assertRaises(InvalidDataType, datatype_factory, 'XXX', 'text')

    def test_datatype_not_allowed_value_creation_strict(self):
        self.assertRaises(ValueError, datatype_factory, 'TM', '999999', validation_level=VALIDATION_LEVEL.STRICT)

    def test_datatype_not_allowed_value_creation(self):
        datatype_factory('TM', '9999')

    def test_create_timestamp_with_offset_by_factory(self):
        tm = datatype_factory('TM', '120000+0000')
        self.assertEqual(tm.classname, 'TM')
        self.assertEqual(tm.offset, '+0000')
        self.assertEqual(tm.to_er7(), '120000+0000')

    def test_create_year_month_date_by_factory(self):
        dt = datatype_factory('DT', '201201')
        self.assertEqual(dt.classname, 'DT')
        self.assertEqual(dt.to_er7(), '201201')

    def test_create_year_month_day_date_by_factory(self):
        dt = datatype_factory('DT', '20120101')
        self.assertEqual(dt.classname, 'DT')
        self.assertEqual(dt.to_er7(), '20120101')

    def test_create_hour_time_by_factory(self):
        tm = datatype_factory('TM', '14')
        self.assertEqual(tm.classname, 'TM')
        self.assertEqual(tm.to_er7(), '14')

    def test_create_datetime_by_factory(self):
        dtm = datatype_factory('DTM', '20130726120252.0590+0200')
        self.assertEqual(dtm.classname, 'DTM')
        self.assertEqual(dtm.to_er7(), '20130726120252.0590+0200')

        dtm = datatype_factory('DTM', '20130726120252.059+0200')
        self.assertEqual(dtm.classname, 'DTM')
        self.assertEqual(dtm.to_er7(), '20130726120252.059+0200')

        dtm = datatype_factory('DTM', '20130726120252.05+0200')
        self.assertEqual(dtm.classname, 'DTM')
        self.assertEqual(dtm.to_er7(), '20130726120252.05+0200')

        dtm = datatype_factory('DTM', '20130726120252.5+0200')
        self.assertEqual(dtm.classname, 'DTM')
        self.assertEqual(dtm.to_er7(), '20130726120252.5+0200')

        dtm = datatype_factory('DTM', '20130726120252+0200')
        self.assertEqual(dtm.classname, 'DTM')
        self.assertEqual(dtm.to_er7(), '20130726120252+0200')

    def test_create_timestamp_by_factory(self):
        dtm = datatype_factory('TM', '120252.0590+0200')
        self.assertEqual(dtm.classname, 'TM')
        self.assertEqual(dtm.to_er7(), '120252.0590+0200')

        dtm = datatype_factory('TM', '120252.059+0200')
        self.assertEqual(dtm.classname, 'TM')
        self.assertEqual(dtm.to_er7(), '120252.059+0200')

        dtm = datatype_factory('TM', '120252.05-0200')
        self.assertEqual(dtm.classname, 'TM')
        self.assertEqual(dtm.to_er7(), '120252.05-0200')

        dtm = datatype_factory('TM', '120252.05+1400')
        self.assertEqual(dtm.classname, 'TM')
        self.assertEqual(dtm.to_er7(), '120252.05+1400')

        dtm = datatype_factory('TM', '120252.5+0200')
        self.assertEqual(dtm.classname, 'TM')
        self.assertEqual(dtm.to_er7(), '120252.5+0200')

        dtm = datatype_factory('TM', '120252-1200')
        self.assertEqual(dtm.classname, 'TM')
        self.assertEqual(dtm.to_er7(), '120252-1200')

    def test_create_nm_by_factory(self):
        nm = datatype_factory('NM', 100000)
        self.assertEqual(nm.classname, 'NM')
        self.assertEqual(nm.to_er7(), '100000')

    def test_create_invalid_nm_by_factory_strict(self):
        self.assertRaises(ValueError, datatype_factory, 'NM', 'aaaaa', validation_level=VALIDATION_LEVEL.STRICT)


class TestDT(unittest.TestCase):

    def test_DT(self):
        date = datetime.strptime('2013', '%Y')
        date1 = datetime.strptime('201307', '%Y%m')
        date2 = datetime.strptime('20130715', '%Y%m%d')
        dt = DT(date, out_format='%Y')
        dt1 = DT(date1, out_format='%Y%m')
        dt2 = DT(date2, out_format='%Y%m%d')
        self.assertEqual(dt.classname, 'DT')
        self.assertEqual(dt.to_er7(), datetime.strftime(date, dt.format))
        self.assertEqual(dt1.to_er7(), datetime.strftime(date1, dt1.format))
        self.assertEqual(dt2.to_er7(), datetime.strftime(date2, dt2.format))

    def test_DT_wrong_format(self):
        self.assertRaises(InvalidDateFormat, DT, datetime.strptime('13', '%y'), out_format='%y')
        self.assertRaises(InvalidDateFormat, DT, datetime.strptime('12', '%m'), out_format='%m')
        self.assertRaises(InvalidDateFormat, DT, datetime.strptime('1202', '%m%d'), out_format='%m%d')
        self.assertRaises(InvalidDateFormat, DT, datetime.strptime('02', '%d'), out_format='%d')

    def test_DT_default_format(self):
        date = datetime.strptime('20130715', '%Y%m%d')
        dt = DT(date)
        self.assertEqual(dt.to_er7(), datetime.strftime(date, dt.format))

    def test_DT_wrong_default_format_strict(self):
        date = datetime.strptime('20', '%H')
        self.assertRaises(InvalidDateFormat, DT, date, out_format='%H', )


class TestTM(unittest.TestCase):

    def test_TM(self):

        time = datetime.strptime('01', '%H')
        time1 = datetime.strptime('0101', '%H%M')
        time2 = datetime.strptime('010111', '%H%M%S')
        time3 = datetime.strptime('010111.1110', '%H%M%S.%f')
        tm = TM(time, out_format='%H')
        tm1 = TM(time1, out_format='%H%M')
        tm2 = TM(time2, out_format='%H%M%S')
        tm3 = TM(time3, out_format='%H%M%S.%f')
        self.assertEqual(tm.classname, 'TM')
        self.assertEqual(tm.to_er7(), '01')
        self.assertEqual(tm1.to_er7(), '0101')
        self.assertEqual(tm2.to_er7(), '010111')
        self.assertEqual(tm3.to_er7(), '010111.1110')

    def test_TM_wrong_format(self):
        tm = datetime.strptime('01', '%I')
        self.assertRaises(InvalidDateFormat, TM, tm, out_format='%I')
        self.assertRaises(InvalidDateFormat, TM, datetime.strptime('12', '%M'), out_format='%M')
        self.assertRaises(InvalidDateFormat, TM, datetime.strptime('1212', '%M%S'), out_format='%M%S')

    def test_TM_default_format(self):
        time = datetime.strptime('010111.1110', '%H%M%S.%f')
        tm = TM(time)
        self.assertEqual(tm.to_er7(), '010111.1110')

    def test_TM_offset(self):
        time = datetime.strptime('0101', '%H%M')
        time2 = datetime.strptime('010111.1110', '%H%M%S.%f')
        tm = TM(time, out_format='%H%M', offset='+0100')
        tm2 = TM(time2, out_format='%H%M%S.%f', offset='-0300')
        TM(time, offset='+0000')
        TM(time, offset='-0000')
        TM(time, offset='+1200')
        TM(time, offset='-1200')
        self.assertEqual(tm.offset, '+0100')
        self.assertEqual(tm2.offset, '-0300')
        self.assertEqual(tm.to_er7(), '0101+0100')  # check if a space is needed between time and offset, or not
        self.assertEqual(tm2.to_er7(), '010111.1110-0300')

    def test_TM_invalid_offset(self):
        self.assertRaises(InvalidDateOffset, TM, datetime.strptime('0101', '%H%M'), offset='+00:00')
        self.assertRaises(InvalidDateOffset, TM, datetime.strptime('0101', '%H%M'), offset='&0100')
        self.assertRaises(InvalidDateOffset, TM, datetime.strptime('0101', '%H%M'), offset='+100')
        self.assertRaises(InvalidDateOffset, TM, datetime.strptime('0101', '%H%M'), offset='+1500')
        self.assertRaises(InvalidDateOffset, TM, datetime.strptime('0101', '%H%M'), offset='-1300')

    def test_TM_custom_microsec_precision(self):
        time = datetime.strptime('011959.1234', '%H%M%S.%f')
        tm = TM(time, microsec_precision=1)
        self.assertEqual(tm.to_er7(), '011959.1')
        tm = TM(time, microsec_precision=2)
        self.assertEqual(tm.to_er7(), '011959.12')
        tm = TM(time, microsec_precision=3)
        self.assertEqual(tm.to_er7(), '011959.123')
        tm = TM(time, microsec_precision=4)
        self.assertEqual(tm.to_er7(), '011959.1234')

    def test_TM_invalid_microsec_precision(self):
        self.assertRaises(InvalidMicrosecondsPrecision, TM, datetime.now(), microsec_precision=0)
        self.assertRaises(InvalidMicrosecondsPrecision, TM, datetime.now(), microsec_precision=5)


class TestDTM(unittest.TestCase):

    def test_DTM(self):
        dtime = datetime.strptime('2013', '%Y')
        dtime1 = datetime.strptime('201307', '%Y%m')
        dtime2 = datetime.strptime('20130715', '%Y%m%d')
        dtime3 = datetime.strptime('01', '%H')
        dtime4 = datetime.strptime('0101', '%H%M')
        dtime5 = datetime.strptime('010111', '%H%M%S')
        dtime6 = datetime.strptime('010111.1110', '%H%M%S.%f')
        dtime7 = datetime.strptime('20130715010111.1110', '%Y%m%d%H%M%S.%f')

        dtm = DTM(dtime, out_format='%Y')
        dtm1 = DTM(dtime1, out_format='%Y%m')
        dtm2 = DTM(dtime2, out_format='%Y%m%d')
        dtm3 = TM(dtime3, out_format='%H')
        dtm4 = TM(dtime4, out_format='%H%M')
        dtm5 = TM(dtime5, out_format='%H%M%S')
        dtm6 = TM(dtime6, out_format='%H%M%S.%f')
        dtm7 = DTM(dtime7, out_format='%Y%m%d%H%M%S.%f')

        self.assertEqual(dtm.classname, 'DTM')
        self.assertEqual(dtm.to_er7(), '2013')
        self.assertEqual(dtm1.to_er7(), '201307')
        self.assertEqual(dtm2.to_er7(), '20130715')
        self.assertEqual(dtm3.to_er7(), '01')
        self.assertEqual(dtm4.to_er7(), '0101')
        self.assertEqual(dtm5.to_er7(), '010111')
        self.assertEqual(dtm6.to_er7(), '010111.1110')
        self.assertEqual(dtm7.to_er7(), '20130715010111.1110')

    def test_DTM_default_format(self):
        dtime = datetime.strptime('20130715 010111.1110', '%Y%m%d %H%M%S.%f')
        dtm = DTM(dtime)
        self.assertEqual(dtm.to_er7(), '20130715010111.1110')

    def test_DTM_wrong_format(self):
        dtime = datetime.strptime('0715010111.111', '%m%d%H%M%S.%f')
        self.assertRaises(InvalidDateFormat, DTM, dtime, out_format='%m%d%H%M%S.%f')

    def test_DTM_offset(self):
        dtime = datetime.strptime('20130715 010111.1110', '%Y%m%d %H%M%S.%f')
        dtm = DTM(dtime, offset='+0100')
        self.assertEqual(dtm.to_er7(), '20130715010111.1110+0100')

    def test_DTM_invalid_offset(self):
        self.assertRaises(InvalidDateOffset, DTM, datetime.strptime('2013', '%Y'), offset='+00:00')
        self.assertRaises(InvalidDateOffset, DTM, datetime.strptime('2013', '%Y'), offset='&0100')
        self.assertRaises(InvalidDateOffset, DTM, datetime.strptime('2013', '%Y'), offset='+100')

    def test_DTM_custom_microsec_precision(self):
        time = datetime.strptime('20130705011959.1234', '%Y%m%d%H%M%S.%f')
        tm = DTM(time, microsec_precision=1)
        self.assertEqual(tm.to_er7(), '20130705011959.1')
        tm = DTM(time, microsec_precision=2)
        self.assertEqual(tm.to_er7(), '20130705011959.12')
        tm = DTM(time, microsec_precision=3)
        self.assertEqual(tm.to_er7(), '20130705011959.123')
        tm = DTM(time, microsec_precision=4)
        self.assertEqual(tm.to_er7(), '20130705011959.1234')

    def test_DTM_invalid_microsec_precision(self):
        self.assertRaises(InvalidMicrosecondsPrecision, DTM, datetime.now(), microsec_precision=0)
        self.assertRaises(InvalidMicrosecondsPrecision, DTM, datetime.now(), microsec_precision=5)


class TestST(unittest.TestCase):

    # Test ST datatype

    def test_ST(self):
        st = ST('Specimen')
        self.assertEqual(st.classname, 'ST')
        self.assertEqual(st.to_er7(), 'Specimen')

    def test_ST_maxlength_strict(self):
        s = 'a' * (ST(' ').max_length + 1)
        self.assertRaises(MaxLengthReached, ST, s, validation_level=VALIDATION_LEVEL.STRICT)

    def test_ST_maxlength(self):
        s = 'a' * (ST(' ').max_length + 100)
        ST(s)

    def test_ST_field_escaping(self):
        st = ST('|field|')
        self.assertEqual(st.to_er7(), '\\F\\field\\F\\')

    def test_ST_component_escape(self):
        st = ST('^component^')
        self.assertEqual(st.to_er7(), '\\S\\component\\S\\')

    def test_ST_subcomponent_escape(self):
        st = ST('&subcomponent&')
        self.assertEqual(st.to_er7(), '\\T\\subcomponent\\T\\')

    def test_ST_repetition_escape(self):
        st = ST('~repetition~')
        self.assertEqual(st.to_er7(), '\\R\\repetition\\R\\')

    def test_ST_highlights(self):
        st = ST('HIGHLIGHTEDTEXTIMPORTANT', highlights=((0, 11), (18, 24)))
        self.assertEqual(st.to_er7(), '\\H\\HIGHLIGHTED\\N\\TEXTIMP\\H\\ORTANT\\N\\')

    def test_ST_invalid_highlight_range(self):
        st = ST('HIGHLIGHTEDTEXTIMPORTANT', highlights=((0, 11), (4, 24)))
        self.assertRaises(InvalidHighlightRange, st.to_er7)
        st = ST('HIGHLIGHTEDTEXTIMPORTANT', highlights=((4, 24), (0, 11)))
        self.assertRaises(InvalidHighlightRange, st.to_er7)
        st = ST('HIGHLIGHTEDTEXTIMPORTANT', highlights=((5, 11), (0, 11)))
        self.assertRaises(InvalidHighlightRange, st.to_er7)
        st = ST('HIGHLIGHTEDTEXTIMPORTANT', highlights=((0, 11), (0, 4)))
        self.assertRaises(InvalidHighlightRange, st.to_er7)

    def test_ST27_truncation_escape(self):
        st = ST27('#truncation#')
        self.assertEqual(st.to_er7(), '\\L\\truncation\\L\\')


class TestFT(unittest.TestCase):

    # Test FT datatype

    def test_FT(self):
        text = 'This is a FT datatype text'
        ft = FT(text)
        self.assertEqual(ft.classname, 'FT')
        self.assertEqual(ft.to_er7(), text)

    def test_FT_maxlength_strict(self):
        ft = 'a' * (FT(' ').max_length + 1)
        self.assertRaises(MaxLengthReached, FT, ft, validation_level=VALIDATION_LEVEL.STRICT)

    def test_FT_maxlength(self):
        ft_str = 'a' * (FT(' ').max_length + 1)
        FT(ft_str)  # no exception is raised here

    def test_FT_field_escaping(self):
        ft = FT('|field|')
        self.assertEqual(ft.to_er7(), '\\F\\field\\F\\')

    def test_FT_component_escape(self):
        ft = FT('^component^')
        self.assertEqual(ft.to_er7(), '\\S\\component\\S\\')

    def test_FT_subcomponent_escape(self):
        ft = FT('&subcomponent&')
        self.assertEqual(ft.to_er7(), '\\T\\subcomponent\\T\\')

    def test_FT_repetition_escape(self):
        ft = FT('~repetition~')
        self.assertEqual(ft.to_er7(), '\\R\\repetition\\R\\')

    def test_FT_highlights(self):
        ft = FT('HIGHLIGHTEDTEXTIMPORTANT', highlights=((0, 11), (18, 24)))
        self.assertEqual(ft.to_er7(), '\\H\\HIGHLIGHTED\\N\\TEXTIMP\\H\\ORTANT\\N\\')

    def test_FT_invalid_highlight_range(self):
        ft = FT('HIGHLIGHTEDTEXTIMPORTANT', highlights=((0, 11), (4, 24)))
        self.assertRaises(InvalidHighlightRange, ft.to_er7)
        ft = FT('HIGHLIGHTEDTEXTIMPORTANT', highlights=((4, 24), (0, 11)))
        self.assertRaises(InvalidHighlightRange, ft.to_er7)
        ft = FT('HIGHLIGHTEDTEXTIMPORTANT', highlights=((5, 11), (0, 11)))
        self.assertRaises(InvalidHighlightRange, ft.to_er7)
        ft = FT('HIGHLIGHTEDTEXTIMPORTANT', highlights=((0, 11), (0, 4)))
        self.assertRaises(InvalidHighlightRange, ft.to_er7)

    def test_FT27_truncation_escape(self):
        ft = FT27('#truncation#')
        self.assertEqual(ft.to_er7(), '\\L\\truncation\\L\\')


class TestID(unittest.TestCase):

    # Test ID datatype

    def test_ID(self):
        id_str = 'This is a ID'
        i = ID(id_str)
        self.assertEqual(i.classname, 'ID')
        self.assertEqual(i.to_er7(), id_str)

    def test_ID_field_escaping(self):
        i = ID('|field|')
        self.assertEqual(i.to_er7(), '\\F\\field\\F\\')

    def test_ID_component_escape(self):
        i = ID('^component^')
        self.assertEqual(i.to_er7(), '\\S\\component\\S\\')

    def test_ID_subcomponent_escape(self):
        i = ID('&subcomponent&')
        self.assertEqual(i.to_er7(), '\\T\\subcomponent\\T\\')

    def test_ID_repetition_escape(self):
        i = ID('~repetition~')
        self.assertEqual(i.to_er7(), '\\R\\repetition\\R\\')

    def test_ID_highlights(self):
        i = ID('HIGHLIGHTEDTEXTIMPORTANT', highlights=((0, 11), (18, 24)))
        self.assertEqual(i.to_er7(), '\\H\\HIGHLIGHTED\\N\\TEXTIMP\\H\\ORTANT\\N\\')

    def test_ID_invalid_highlight_range(self):
        i = ID('HIGHLIGHTEDTEXTIMPORTANT', highlights=((0, 11), (4, 24)))
        self.assertRaises(InvalidHighlightRange, i.to_er7)
        i = ID('HIGHLIGHTEDTEXTIMPORTANT', highlights=((4, 24), (0, 11)))
        self.assertRaises(InvalidHighlightRange, i.to_er7)
        i = ID('HIGHLIGHTEDTEXTIMPORTANT', highlights=((5, 11), (0, 11)))
        self.assertRaises(InvalidHighlightRange, i.to_er7)
        i = ID('HIGHLIGHTEDTEXTIMPORTANT', highlights=((0, 11), (0, 4)))
        self.assertRaises(InvalidHighlightRange, i.to_er7)

    def test_ID27_truncation_escape(self):
        i = ID27('#truncation#')
        self.assertEqual(i.to_er7(), '\\L\\truncation\\L\\')


class TestIS(unittest.TestCase):

    # Test IS datatype

    def test_IS(self):
        is_str = 'This is a IS'
        is_obj = IS(is_str)
        self.assertEqual(is_obj.classname, 'IS')
        self.assertEqual(is_obj.to_er7(), is_str)

    def test_IS_maxlength_strict(self):
        is_str = 'a' * (IS(' ').max_length + 1)
        self.assertRaises(MaxLengthReached, IS, is_str, validation_level=VALIDATION_LEVEL.STRICT)

    def test_IS_field_escaping(self):
        i = IS('|field|')
        self.assertEqual(i.to_er7(), '\\F\\field\\F\\')

    def test_IS_component_escape(self):
        i = IS('^component^')
        self.assertEqual(i.to_er7(), '\\S\\component\\S\\')

    def test_IS_subcomponent_escape(self):
        i = IS('&subcomponent&')
        self.assertEqual(i.to_er7(), '\\T\\subcomponent\\T\\')

    def test_IS_repetition_escape(self):
        i = IS('~repetition~')
        self.assertEqual(i.to_er7(), '\\R\\repetition\\R\\')

    def test_IS_highlights(self):
        i = IS('HIGHLIGHTEDTEXTIMPORTANT', highlights=((0, 11), (18, 24)))
        self.assertEqual(i.to_er7(), '\\H\\HIGHLIGHTED\\N\\TEXTIMP\\H\\ORTANT\\N\\')

    def test_ST_invalid_highlight_range(self):
        st = ST('HIGHLIGHTEDTEXTIMPORTANT', highlights=((0, 11), (4, 24)))
        self.assertRaises(InvalidHighlightRange, st.to_er7)
        st = ST('HIGHLIGHTEDTEXTIMPORTANT', highlights=((4, 24), (0, 11)))
        self.assertRaises(InvalidHighlightRange, st.to_er7)
        st = ST('HIGHLIGHTEDTEXTIMPORTANT', highlights=((5, 11), (0, 11)))
        self.assertRaises(InvalidHighlightRange, st.to_er7)
        st = ST('HIGHLIGHTEDTEXTIMPORTANT', highlights=((0, 11), (0, 4)))
        self.assertRaises(InvalidHighlightRange, st.to_er7)

    def test_IS27_truncation_escape(self):
        i = IS27('#truncation#')
        self.assertEqual(i.to_er7(), '\\L\\truncation\\L\\')


class TestTX(unittest.TestCase):

    # Test TX datatype

    def test_TX(self):
        text = 'This is a TX datatype text'
        tx = TX(text)
        self.assertEqual(tx.classname, 'TX')
        self.assertEqual(tx.to_er7(), text)

    def test_TX_maxlength_strict(self):
        tx = 'a' * (TX(' ').max_length + 1)
        self.assertRaises(MaxLengthReached, TX, tx, validation_level=VALIDATION_LEVEL.STRICT)

    def test_TX_maxlength(self):
        tx_str = 'a' * (TX(' ').max_length + 1)
        TX(tx_str)

    def test_TX_field_escaping(self):
        tx = TX('|field|')
        self.assertEqual(tx.to_er7(), '\\F\\field\\F\\')

    def test_TX_component_escape(self):
        tx = TX('^component^')
        self.assertEqual(tx.to_er7(), '\\S\\component\\S\\')

    def test_TX_subcomponent_escape(self):
        tx = TX('&subcomponent&')
        self.assertEqual(tx.to_er7(), '\\T\\subcomponent\\T\\')

    def test_TX_repetition_escape(self):
        tx = TX('~repetition~')
        self.assertEqual(tx.to_er7(), '\\R\\repetition\\R\\')

    def test_TX_highlights(self):
        tx = TX('HIGHLIGHTEDTEXTIMPORTANT', highlights=((0, 11), (18, 24)))
        self.assertEqual(tx.to_er7(), '\\H\\HIGHLIGHTED\\N\\TEXTIMP\\H\\ORTANT\\N\\')

    def test_TX_invalid_highlight_range(self):
        tx = TX('HIGHLIGHTEDTEXTIMPORTANT', highlights=((0, 11), (4, 24)))
        self.assertRaises(InvalidHighlightRange, tx.to_er7)
        tx = TX('HIGHLIGHTEDTEXTIMPORTANT', highlights=((4, 24), (0, 11)))
        self.assertRaises(InvalidHighlightRange, tx.to_er7)
        tx = TX('HIGHLIGHTEDTEXTIMPORTANT', highlights=((5, 11), (0, 11)))
        self.assertRaises(InvalidHighlightRange, tx.to_er7)
        tx = TX('HIGHLIGHTEDTEXTIMPORTANT', highlights=((0, 11), (0, 4)))
        self.assertRaises(InvalidHighlightRange, tx.to_er7)

    def test_TX27_truncation_escape(self):
        tx = TX27('#truncation#')
        self.assertEqual(tx.to_er7(), '\\L\\truncation\\L\\')


class TestGTS(unittest.TestCase):

    # Test GTS Datatype

    def test_GTS(self):
        text = 'This is a GTS datatype text'
        gts = GTS(text)
        self.assertEqual(gts.classname, 'GTS')
        self.assertEqual(gts.to_er7(), text)

    def test_GTS_maxlength_strict(self):
        gts = 'a' * (GTS(' ').max_length + 1)
        self.assertRaises(MaxLengthReached, GTS, gts, validation_level=VALIDATION_LEVEL.STRICT)

    def test_GTS_maxlength(self):
        gts_str = 'a' * (GTS(' ').max_length + 1)
        GTS(gts_str)

    def test_GTS_field_escaping(self):
        gts = GTS('|field|')
        self.assertEqual(gts.to_er7(), '\\F\\field\\F\\')

    def test_GTS_component_escape(self):
        gts = GTS('^component^')
        self.assertEqual(gts.to_er7(), '\\S\\component\\S\\')

    def test_GTS_subcomponent_escape(self):
        gts = GTS('&subcomponent&')
        self.assertEqual(gts.to_er7(), '\\T\\subcomponent\\T\\')

    def test_GTS_repetition_escape(self):
        gts = GTS('~repetition~')
        self.assertEqual(gts.to_er7(), '\\R\\repetition\\R\\')

    def test_GTS_highlights(self):
        gts = GTS('HIGHLIGHTEDTEXTIMPORTANT', highlights=((0, 11), (18, 24)))
        self.assertEqual(gts.to_er7(), '\\H\\HIGHLIGHTED\\N\\TEXTIMP\\H\\ORTANT\\N\\')

    def test_GTS_invalid_highlight_range(self):
        gts = GTS('HIGHLIGHTEDTEXTIMPORTANT', highlights=((0, 11), (4, 24)))
        self.assertRaises(InvalidHighlightRange, gts.to_er7)
        gts = GTS('HIGHLIGHTEDTEXTIMPORTANT', highlights=((4, 24), (0, 11)))
        self.assertRaises(InvalidHighlightRange, gts.to_er7)
        gts = GTS('HIGHLIGHTEDTEXTIMPORTANT', highlights=((5, 11), (0, 11)))
        self.assertRaises(InvalidHighlightRange, gts.to_er7)
        gts = GTS('HIGHLIGHTEDTEXTIMPORTANT', highlights=((0, 11), (0, 4)))
        self.assertRaises(InvalidHighlightRange, gts.to_er7)

    def test_GTS27_truncation_escape(self):
        gts = GTS27('#truncation#')
        self.assertEqual(gts.to_er7(), '\\L\\truncation\\L\\')


class TestNM(unittest.TestCase):

    # Test NM datatype

    def test_NM(self):
        num = NM(Decimal(1234))
        self.assertEqual(num.classname, 'NM')
        self.assertEqual(num.to_er7(), '1234')
        num = 1234
        NM(num)
        num = float(1234.54)
        NM(num)

    def test_NM_maxlength_strict(self):
        num = Decimal(1000000000000000000000000000000000000000000000000000000000000000000000000000)
        self.assertRaises(MaxLengthReached, NM, num, validation_level=VALIDATION_LEVEL.STRICT)

    def test_NM_maxlength(self):
        num = Decimal(1000000000000000000000000000000000000000000000000000000000000000000000000000)
        nm = NM(num)
        self.assertEqual(nm.to_er7(), '1000000000000000000000000000000000000000000000000000000000000000000000000000')

    def test_invalid_NM(self):
        self.assertRaises(ValueError, NM, 'aaaaa')


class TestSI(unittest.TestCase):

    # Test SI datatype

    def test_SI(self):
        si = SI(1234)
        self.assertEqual(si.classname, 'SI')
        self.assertEqual(si.to_er7(), '1234')

    def test_SI_maxlength_strict(self):
        si = 10000
        self.assertRaises(MaxLengthReached, SI, si, validation_level=VALIDATION_LEVEL.STRICT)

    def test_SI_maxlength(self):
        SI(10000)  # no exception is raised here

    def test_invalid_SI(self):
        self.assertRaises(ValueError, SI, 'aaaaaa')


class TestSNM(unittest.TestCase):

    # Test SNM Datatype

    def test_SNM(self):
        text = 'This is a SNM datatype text'
        snm = SNM(text)
        self.assertEqual(snm.classname, 'SNM')
        self.assertEqual(snm.to_er7(), text)

    def test_SNM_field_escaping(self):
        snm = SNM('|field|')
        self.assertEqual(snm.to_er7(), '\\F\\field\\F\\')

    def test_SNM_component_escape(self):
        snm = SNM('^component^')
        self.assertEqual(snm.to_er7(), '\\S\\component\\S\\')

    def test_SNM_subcomponent_escape(self):
        snm = SNM('&subcomponent&')
        self.assertEqual(snm.to_er7(), '\\T\\subcomponent\\T\\')

    def test_SNM_repetition_escape(self):
        snm = SNM('~repetition~')
        self.assertEqual(snm.to_er7(), '\\R\\repetition\\R\\')

    def test_SNM_highlights(self):
        snm = SNM('HIGHLIGHTEDTEXTIMPORTANT', highlights=((0, 11), (18, 24)))
        self.assertEqual(snm.to_er7(), '\\H\\HIGHLIGHTED\\N\\TEXTIMP\\H\\ORTANT\\N\\')

    def test_SNM_invalid_highlight_range(self):
        snm = SNM('HIGHLIGHTEDTEXTIMPORTANT', highlights=((0, 11), (4, 24)))
        self.assertRaises(InvalidHighlightRange, snm.to_er7)
        snm = SNM('HIGHLIGHTEDTEXTIMPORTANT', highlights=((4, 24), (0, 11)))
        self.assertRaises(InvalidHighlightRange, snm.to_er7)
        snm = SNM('HIGHLIGHTEDTEXTIMPORTANT', highlights=((5, 11), (0, 11)))
        self.assertRaises(InvalidHighlightRange, snm.to_er7)
        snm = SNM('HIGHLIGHTEDTEXTIMPORTANT', highlights=((0, 11), (0, 4)))
        self.assertRaises(InvalidHighlightRange, snm.to_er7)

    def test_SNM_truncation_escape(self):
        snm = SNM('#truncation#')
        self.assertEqual(snm.to_er7(), '\\L\\truncation\\L\\')


class TestTN(unittest.TestCase):

    # Test TN Datatype

    def test_TN(self):
        text = '(111)999-999-222X111B222CTEXT'
        tn = TN(text)
        self.assertEqual(tn.classname, 'TN')
        self.assertEqual(tn.to_er7(), text)

    def test_TN_invalid_value(self):
        self.assertRaises(ValueError, TN, 'invalid_value')

    def test_TN_field_escaping(self):
        tn = TN('(111)999-999-222X111B222C|field|')
        self.assertEqual(tn.to_er7(), '(111)999-999-222X111B222C\\F\\field\\F\\')

    def test_TN_component_escape(self):
        tn = TN('(111)999-999-222X111B222C^component^')
        self.assertEqual(tn.to_er7(), '(111)999-999-222X111B222C\\S\\component\\S\\')

    def test_TN_subcomponent_escape(self):
        tn = TN('(111)999-999-222X111B222C&subcomponent&')
        self.assertEqual(tn.to_er7(), '(111)999-999-222X111B222C\\T\\subcomponent\\T\\')

    def test_TN_repetition_escape(self):
        tn = TN('(111)999-999-222X111B222C~repetition~')
        self.assertEqual(tn.to_er7(), '(111)999-999-222X111B222C\\R\\repetition\\R\\')


if __name__ == '__main__':
    unittest.main()
