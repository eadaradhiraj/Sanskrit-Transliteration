import unittest
from sanskrit_transliteration import transliterate


class TestCases(unittest.TestCase):
    def test_hk_to_skt(self):
        self.assertEqual(
            transliterate(
                text="G",
                from_scheme="HK",
                to_scheme="SKT"
            ),
            "ङ्"
        )
        self.assertEqual(
            transliterate(
                text="aGgaH",
                from_scheme="HK",
                to_scheme="SKT"
            ),
            "अङ्गः"
        )
        self.assertEqual(
            transliterate(
                text="jJAnam",
                from_scheme="HK",
                to_scheme="SKT"
            ),
            "ज्ञानम्"
        )
        self.assertEqual(
            transliterate(
                text="RSiH",
                from_scheme="HK",
                to_scheme="SKT"
            ),
            "ऋषिः"
        )
        self.assertEqual(
            transliterate(
                text="|RSiH",
                from_scheme="HK",
                to_scheme="SKT"
            ),
            "।ऋषिः"
        )
        self.assertEqual(
            transliterate(
                text="kaNThakam",
                from_scheme="HK",
                to_scheme="SKT"
            ),
            "कण्ठकम्"
        )
        self.assertEqual(
            transliterate(
                text="pArthAya pratibodhitAM bhagavatA nArAyaNena svayam vyAsena grathitAM purANamuninA madhye "
                     "mahAbhArate",
                from_scheme="HK",
                to_scheme="SKT"
            ),
            "पार्थाय प्रतिबोधितां भगवता नारायणेन स्वयम् व्यासेन ग्रथितां पुराणमुनिना मध्ये महाभारते"
        )
        self.assertEqual(
            transliterate(
                text="rAmaH iva, 123|",
                from_scheme="HK",
                to_scheme="SKT"
            ),
            "रामः इव, १२३।"
        )
        self.assertEqual(
            transliterate(
                text="||auau||",
                from_scheme="HK",
                to_scheme="SKT"
            ),
            "।।औऔ।।"
        )
        self.assertEqual(
            transliterate(
                text="DhuNDhikA'pi",
                from_scheme="HK",
                to_scheme="SKT"
            ),
            "ढुण्ढिकाऽपि"
        )
        self.assertEqual(
            transliterate(
                text="hara hara mahAdeva",
                from_scheme="HK",
                to_scheme="SKT"
            ),
            "हर हर महादेव"
        )
        self.assertEqual(
            transliterate(
                text="ataeva",
                from_scheme="HK",
                to_scheme="SKT"
            ),
            "अतएव"
        )
        self.assertEqual(
            transliterate(
                text="pitRRNAm kRte",
                from_scheme="HK",
                to_scheme="SKT"
            ),
            "पितॄणाम् कृते"
        )
        self.assertEqual(
            transliterate(
                text="|.kRSNaM, vande| jagadgurum",
                from_scheme="HK",
                to_scheme="SKT"
            ),
            "।.कृष्णं, वन्दे। जगद्गुरुम्"
        )
        self.assertEqual(
            transliterate(
                text="|.kRSNaM, vande| jagadgurum|",
                from_scheme="HK",
                to_scheme="SKT"
            ),
            "।.कृष्णं, वन्दे। जगद्गुरुम्।"
        )
        self.assertEqual(
            transliterate(
                text="ahiMsA",
                from_scheme="HK",
                to_scheme="SKT"
            ),
            "अहिंसा"
        )

    def test_skt_to_hk(self):
        self.assertEqual(
            transliterate(
                text="ङ्",
                from_scheme="SKT",
                to_scheme="HK"
            ),
            "G"
        )
        self.assertEqual(
            transliterate(
                text="ज्ञानम्",
                from_scheme="SKT",
                to_scheme="HK"
            ),
            "jJAnam"
        )
        self.assertEqual(
            transliterate(
                text="रामः इव, १२३।",
                from_scheme="SKT",
                to_scheme="HK"
            ),
            "rAmaH iva, 123|"
        )
        self.assertEqual(
            transliterate(
                text="कण्ठकम्",
                from_scheme="SKT",
                to_scheme="HK"
            ),
            "kaNThakam"
        )
        self.assertEqual(
            transliterate(
                text="ढुण्ढिकाऽपि",
                from_scheme="SKT",
                to_scheme="HK"
            ),
            "DhuNDhikA'pi"
        )
        self.assertEqual(
            transliterate(
                text="औऔ",
                from_scheme="SKT",
                to_scheme="HK"
            ),
            "auau"
        )
        self.assertEqual(
            transliterate(
                text="पार्थाय प्रतिबोधितां भगवता नारायणेन स्वयम् व्यासेन ग्रथितां पुराणमुनिना मध्ये महाभारते",
                from_scheme="SKT",
                to_scheme="HK"
            ),
            "pArthAya pratibodhitAM bhagavatA nArAyaNena svayam vyAsena grathitAM purANamuninA "
            "madhye mahAbhArate"
        )
        self.assertEqual(
            transliterate(
                text="हर हर महादेव",
                from_scheme="SKT",
                to_scheme="HK"
            ),
            "hara hara mahAdeva"
        )
        self.assertEqual(
            transliterate(
                text="अतएव",
                from_scheme="SKT",
                to_scheme="HK"
            ),
            "ataeva"
        )
        self.assertEqual(
            transliterate(
                text="पितॄणाम् कृते",
                from_scheme="SKT",
                to_scheme="HK"
            ),
            "pitRRNAm kRte"
        )
        self.assertEqual(
            transliterate(
                text="।.कृष्णं, वन्दे। जगद्गुरुम्",
                from_scheme="SKT",
                to_scheme="HK"
            ),
            "|.kRSNaM, vande| jagadgurum"
        )
        self.assertEqual(
            transliterate(
                text="अहिंसा",
                from_scheme="SKT",
                to_scheme="HK"
            ),
            "ahiMsA"
        )
        self.assertEqual(
            transliterate(
                text="ऋषिः",
                from_scheme="SKT",
                to_scheme="HK"
            ),
            "RSiH"
        )
        self.assertEqual(
            transliterate(
                text="।ऋषिः",
                from_scheme="SKT",
                to_scheme="HK"
            ),
            "|RSiH"
        )


if __name__ == '__main__':
    unittest.main()
