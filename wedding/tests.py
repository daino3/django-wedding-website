# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .models import SiteSection


class SiteSectionTestCase(TestCase):
    def setUp(self):
        self.section_A = SiteSection(name="Section A", order=1, content="A")
        self.section_B = SiteSection(name="Section B", order=2, content="B")
        self.section_C = SiteSection(name="Section C", order=3, content="C")

        self.section_A.save()
        self.section_B.save()
        self.section_C.save()

    def test_reordering_a_section(self):
        self.section_C.order = 1
        self.section_C.save()
        sections = [sec for sec in SiteSection.objects.all().order_by('order')]
        assert sections[0].name == "Section C"
        assert sections[1].name == "Section A"
        assert sections[2].name == "Section B"

    def test_creating_a_new_section(self):
        SiteSection(name="Section D", order=2, content="D").save()

        sections = [sec for sec in SiteSection.objects.all().order_by('order')]
        assert sections[0].name == "Section A"
        assert sections[1].name == "Section D"
        assert sections[2].name == "Section B"
        assert sections[3].name == "Section C"

    def test_deleting_a_section(self):
        self.section_B.delete()

        sections = [sec for sec in SiteSection.objects.all().order_by('order')]
        assert sections[0].name == "Section A"
        assert sections[1].name == "Section C"