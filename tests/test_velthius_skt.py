import unittest

from sanskrit_transliteration import transliterate


class TestCases(unittest.TestCase):
    def test_skt_to_vel(self):
        self.assertEqual(
            transliterate(
                text='ङ्',
                from_scheme="SKT",
                to_scheme="VELTHIUS"
            ),
            '"n'
        )
        self.assertEqual(
            transliterate(
                text='अङ्गः',
                from_scheme="SKT",
                to_scheme="VELTHIUS"
            ),
            'a"nga.h'
        )
        self.assertEqual(
            transliterate(
                text='ज्ञानम्',
                from_scheme="SKT",
                to_scheme="VELTHIUS"
            ),
            "j~naanam"
        )
        self.assertEqual(
            transliterate(
                text="ऋषिः",
                from_scheme="SKT",
                to_scheme="VELTHIUS"
            ),
            ".r.si.h"
        )
        self.assertEqual(
            transliterate(
                text="।ऋषिः",
                from_scheme="SKT",
                to_scheme="VELTHIUS"
            ),
            "..r.si.h"
        )
        self.assertEqual(
            transliterate(
                text="कण्ठकम्",
                from_scheme="SKT",
                to_scheme="VELTHIUS"
            ),
            "ka.n.thakam"
        )
        self.assertEqual(
            transliterate(
                text="पार्थाय प्रतिबोधितां भगवता नारायणेन स्वयम् व्यासेन ग्रथितां पुराणमुनिना मध्ये महाभारते",
                from_scheme="SKT",
                to_scheme="VELTHIUS"
            ),
            "paarthaaya pratibodhitaa.m bhagavataa naaraaya.nena svayam vyaasena grathitaa.m puraa.namuninaa "
            "madhye mahaabhaarate"
        )
        self.assertEqual(
            transliterate(
                text="रामः इव, १२३।",
                from_scheme="SKT",
                to_scheme="VELTHIUS"
            ),
            "raama.h iva, 123."
        )
        self.assertEqual(
            transliterate(
                text="औऔ",
                from_scheme="SKT",
                to_scheme="VELTHIUS"
            ),
            "auau"
        )
        self.assertEqual(
            transliterate(
                text="हर हर महादेव",
                from_scheme="SKT",
                to_scheme="VELTHIUS"
            ),
            "hara hara mahaadeva"
        )
        self.assertEqual(
            transliterate(
                text="अतएव",
                from_scheme="SKT",
                to_scheme="VELTHIUS"
            ),
            "ataeva"
        )
        self.assertEqual(
            transliterate(
                text="ढुण्ढिकाऽपि",
                from_scheme="SKT",
                to_scheme="VELTHIUS"
            ),
            ".dhu.n.dhikaa.api"
        )
        self.assertEqual(
            transliterate(
                text="पितॄणाम् कृते",
                from_scheme="SKT",
                to_scheme="VELTHIUS"
            ),
            "pit.rr.naam k.rte"
        )
        self.assertEqual(
            transliterate(
                text="।.कृष्णं, वन्दे। जगद्गुरुम्",
                from_scheme="SKT",
                to_scheme="VELTHIUS"
            ),
            "..k.r.s.na.m, vande. jagadgurum"
        )
        self.assertEqual(
            transliterate(
                text="अहिंसा",
                from_scheme="SKT",
                to_scheme="VELTHIUS"
            ),
            "ahi.msaa"
        )

    def test_vel_to_skt(self):
        self.assertEqual(
            transliterate(
                text='"n',
                from_scheme="VELTHIUS",
                to_scheme="SKT"
            ),
            "ङ्"
        )
        self.assertEqual(
            transliterate(
                text='a"nga.h',
                from_scheme="VELTHIUS",
                to_scheme="SKT"
            ),
            "अङ्गः"
        )
        self.assertEqual(
            transliterate(
                text='j~naanam',
                from_scheme="VELTHIUS",
                to_scheme="SKT"
            ),
            "ज्ञानम्"
        )
        self.assertEqual(
            transliterate(
                text="paarthaaya pratibodhitaa.m bhagavataa naaraaya.nena svayam vyaasena grathitaa.m puraa.namuninaa "
                     "madhye mahaabhaarate",
                from_scheme="VELTHIUS",
                to_scheme="SKT"
            ),
            "पार्थाय प्रतिबोधितां भगवता नारायणेन स्वयम् व्यासेन ग्रथितां पुराणमुनिना मध्ये महाभारते"
        )
        self.assertEqual(
            transliterate(
                text="raama.h iva, 123.",
                from_scheme="VELTHIUS",
                to_scheme="SKT"
            ),
            "रामः इव, १२३।"
        )
        self.assertEqual(
            transliterate(
                text='a"nga.h',
                from_scheme="VELTHIUS",
                to_scheme="SKT"
            ),
            "अङ्गः"
        )
        self.assertEqual(
            transliterate(
                text='j~naanam',
                from_scheme="VELTHIUS",
                to_scheme="SKT"
            ),
            "ज्ञानम्"
        )
        self.assertEqual(
            transliterate(
                text=".dhu.n.dhikaa.api",
                from_scheme="VELTHIUS",
                to_scheme="SKT"
            ),
            "ढुण्ढिकाऽपि"
        )
        self.assertEqual(
            transliterate(
                text="auau",
                from_scheme="VELTHIUS",
                to_scheme="SKT"
            ),
            "औऔ"
        )
        self.assertEqual(
            transliterate(
                text="hara hara mahaadeva",
                from_scheme="VELTHIUS",
                to_scheme="SKT"
            ),
            "हर हर महादेव"
        )
        self.assertEqual(
            transliterate(
                text="ataeva",
                from_scheme="VELTHIUS",
                to_scheme="SKT"
            ),
            "अतएव"
        )
        self.assertEqual(
            transliterate(
                text="pit.rr.naam k.rte",
                from_scheme="VELTHIUS",
                to_scheme="SKT"
            ),
            "पितॄणाम् कृते"
        )
        self.assertEqual(
            transliterate(
                text="ka.n.thakam",
                from_scheme="VELTHIUS",
                to_scheme="SKT"
            ),
            "कण्ठकम्"
        )
        self.assertEqual(
            transliterate(
                text="..k.r.s.na.m, vande. jagadgurum",
                from_scheme="VELTHIUS",
                to_scheme="SKT"
            ),
            "।।कृष्णं, वन्दे। जगद्गुरुम्"
        )
        self.assertEqual(
            transliterate(
                text="ahi.msaa",
                from_scheme="VELTHIUS",
                to_scheme="SKT"
            ),
            "अहिंसा"
        )
        self.assertEqual(
            transliterate(
                text=".r.si.h",
                from_scheme="VELTHIUS",
                to_scheme="SKT"
            ),
            "ऋषिः"
        )
        self.assertEqual(
            transliterate(
                text="..r.si.h",
                from_scheme="VELTHIUS",
                to_scheme="SKT"
            ),
            "।ऋषिः"
        )


if __name__ == '__main__':
    unittest.main()
