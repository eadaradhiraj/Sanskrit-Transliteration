import unittest
from sanskrit_transliteration import transliterate


class TestCases(unittest.TestCase):
    def test_hk_to_velthius(self):
        self.assertEqual(
            transliterate(
                text='G',
                from_scheme="HK",
                to_scheme="VELTHIUS"
            ),
            '"n'
        )
        self.assertEqual(
            transliterate(
                text='aGgaH',
                from_scheme="HK",
                to_scheme="VELTHIUS"
            ),
            'a"nga.h'
        )
        self.assertEqual(
            transliterate(
                text='jJAnam',
                from_scheme="HK",
                to_scheme="VELTHIUS"
            ),
            'j~naanam'
        )
        self.assertEqual(
            transliterate(
                text="RSiH",
                from_scheme="HK",
                to_scheme="VELTHIUS"
            ),
            ".r.si.h"
        )
        self.assertEqual(
            transliterate(
                text="|RSiH",
                from_scheme="HK",
                to_scheme="VELTHIUS"
            ),
            "..r.si.h"
        )
        self.assertEqual(
            transliterate(
                text="kaNThakam",
                from_scheme="HK",
                to_scheme="VELTHIUS"
            ),
            "ka.n.thakam"
        )
        self.assertEqual(
            transliterate(
                text="pArthAya pratibodhitAM bhagavatA nArAyaNena svayam vyAsena grathitAM purANamuninA madhye mahAbhArate",
                from_scheme="HK",
                to_scheme="VELTHIUS"
            ),
            "paarthaaya pratibodhitaa.m bhagavataa naaraaya.nena svayam vyaasena grathitaa.m puraa.namuninaa "
            "madhye mahaabhaarate"
        )
        self.assertEqual(
            transliterate(
                text="rAmaH iva, 123|",
                from_scheme="HK",
                to_scheme="VELTHIUS"
            ),
            "raama.h iva, 123."
        )
        self.assertEqual(
            transliterate(
                text="auau",
                from_scheme="HK",
                to_scheme="VELTHIUS"
            ),
            "auau"
        )
        self.assertEqual(
            transliterate(
                text="||auau||",
                from_scheme="HK",
                to_scheme="VELTHIUS"
            ),
            "..auau.."
        )
        self.assertEqual(
            transliterate(
                text="hara hara mahAdeva",
                from_scheme="HK",
                to_scheme="VELTHIUS"
            ),
            "hara hara mahaadeva"
        )
        self.assertEqual(
            transliterate(
                text="ataeva",
                from_scheme="HK",
                to_scheme="VELTHIUS"
            ),
            "ataeva"
        )
        self.assertEqual(
            transliterate(
                text="DhuNDhikA'pi",
                from_scheme="HK",
                to_scheme="VELTHIUS"
            ),
            ".dhu.n.dhikaa.api"
        )
        self.assertEqual(
            transliterate(
                text="pitRRNAm kRte",
                from_scheme="HK",
                to_scheme="VELTHIUS"
            ),
            "pit.rr.naam k.rte"
        )
        self.assertEqual(
            transliterate(
                text="|.kRSNaM, vande| jagadgurum",
                from_scheme="HK",
                to_scheme="VELTHIUS"
            ),
            "..k.r.s.na.m, vande. jagadgurum"
        )
        self.assertEqual(
            transliterate(
                text="ahiMsA",
                from_scheme="HK",
                to_scheme="VELTHIUS"
            ),
            "ahi.msaa"
        )

    def test_velthius_to_hk(self):
        self.assertEqual(
            transliterate(
                text='a"nga.h',
                from_scheme="VELTHIUS",
                to_scheme="HK"
            ),
            'aGgaH'
        )
        self.assertEqual(
            transliterate(
                text='j~naanam',
                from_scheme="VELTHIUS",
                to_scheme="HK"
            ),
            'jJAnam'
        )
        self.assertEqual(
            transliterate(
                text="paarthaaya pratibodhitaa.m bhagavataa naaraaya.nena svayam vyaasena grathitaa.m puraa.namuninaa "
                     "madhye mahaabhaarate",
                from_scheme="VELTHIUS",
                to_scheme="HK"
            ),
            "pArthAya pratibodhitAM bhagavatA nArAyaNena svayam vyAsena grathitAM purANamuninA madhye mahAbhArate"
        )
        self.assertEqual(
            transliterate(
                text="raama.h iva, 123.",
                from_scheme="VELTHIUS",
                to_scheme="HK"
            ),
            "rAmaH iva, 123|"
        )
        self.assertEqual(
            transliterate(
                text=".dhu.n.dhikaa.api",
                from_scheme="VELTHIUS",
                to_scheme="HK"
            ),
            "DhuNDhikA'pi"
        )
        self.assertEqual(
            transliterate(
                text="auau",
                from_scheme="VELTHIUS",
                to_scheme="HK"
            ),
            "auau"
        )
        self.assertEqual(
            transliterate(
                text="hara hara mahaadeva",
                from_scheme="VELTHIUS",
                to_scheme="HK"
            ),
            "hara hara mahAdeva"
        )
        self.assertEqual(
            transliterate(
                text="ataeva",
                from_scheme="VELTHIUS",
                to_scheme="HK"
            ),
            "ataeva"
        )
        self.assertEqual(
            transliterate(
                text="pit.rr.naam k.rte",
                from_scheme="VELTHIUS",
                to_scheme="HK"
            ),
            "pitRRNAm kRte"
        )
        self.assertEqual(
            transliterate(
                text="ka.n.thakam",
                from_scheme="VELTHIUS",
                to_scheme="HK"
            ),
            "kaNThakam"
        )
        self.assertEqual(
            transliterate(
                text="..k.r.s.na.m, vande. jagadgurum",
                from_scheme="VELTHIUS",
                to_scheme="HK"
            ),
            "||kRSNaM, vande| jagadgurum"
        )
        self.assertEqual(
            transliterate(
                text="ahi.msaa",
                from_scheme="VELTHIUS",
                to_scheme="HK"
            ),
            "ahiMsA"
        )
        self.assertEqual(
            transliterate(
                text=".r.si.h",
                from_scheme="VELTHIUS",
                to_scheme="HK"
            ),
            "RSiH"
        )
        self.assertEqual(
            transliterate(
                text="..r.si.h",
                from_scheme="VELTHIUS",
                to_scheme="HK"
            ),
            "|RSiH"
        )


if __name__ == '__main__':
    unittest.main()
