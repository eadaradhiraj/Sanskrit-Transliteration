import unittest
from sanskrit_transliteration import transliterate


class TestCases(unittest.TestCase):
    def test_wx_to_skt(self):
        self.assertEqual(
            transliterate(text="f", from_scheme="WX", to_scheme="SKT"),
            "ङ्"
        )
        self.assertEqual(
            transliterate(text="afgaH", from_scheme="WX", to_scheme="SKT"),
            "अङ्गः"
        )
        self.assertEqual(
            transliterate(text="jFAnam", from_scheme="WX", to_scheme="SKT"),
            "ज्ञानम्"
        )
        self.assertEqual(
            transliterate(text="qRiH", from_scheme="WX", to_scheme="SKT"),
            "ऋषिः"
        )
        self.assertEqual(
            transliterate(text=".qRiH", from_scheme="WX", to_scheme="SKT"),
            "।ऋषिः"
        )
        self.assertEqual(
            transliterate(text="kaNTakam", from_scheme="WX", to_scheme="SKT"),
            "कण्ठकम्"
        )
        self.assertEqual(
            transliterate(
                text="pArWAya prawiboXiwAM BagavawA nArAyaNena svayam vyAsena graWiwAM purANamuninA maXye mahABArawe",
                from_scheme="WX", to_scheme="SKT"),
            "पार्थाय प्रतिबोधितां भगवता नारायणेन स्वयम् व्यासेन ग्रथितां पुराणमुनिना मध्ये महाभारते"
        )
        self.assertEqual(
            transliterate(text="rAmaH iva, 123.", from_scheme="WX", to_scheme="SKT"),
            "रामः इव, १२३।"
        )
        self.assertEqual(
            transliterate(text="DuNDikAZpi", from_scheme="WX", to_scheme="SKT"),
            "ढुण्ढिकाऽपि"
        )
        self.assertEqual(
            transliterate(text="hara hara mahAxeva", from_scheme="WX", to_scheme="SKT"),
            "हर हर महादेव"
        )
        self.assertEqual(
            transliterate(text="awaeva", from_scheme="WX", to_scheme="SKT"),
            "अतएव"
        )
        self.assertEqual(
            transliterate(text="piwQNAm kqwe", from_scheme="WX", to_scheme="SKT"),
            "पितॄणाम् कृते"
        )
        self.assertEqual(
            transliterate(text="|.kqRNaM, vanxe| jagaxgurum", from_scheme="WX", to_scheme="SKT"),
            "|।कृष्णं, वन्दे| जगद्गुरुम्"
        )
        self.assertEqual(
            transliterate(text="..kqRNaM, vanxe. jagaxgurum.", from_scheme="WX", to_scheme="SKT"),
            "।।कृष्णं, वन्दे। जगद्गुरुम्।"
        )
        self.assertEqual(
            transliterate(text="ahiMsA", from_scheme="WX", to_scheme="SKT"),
            "अहिंसा"
        )

    def test_slp1_to_skt(self):
        self.assertEqual(
            transliterate(text="N", from_scheme="SLP1", to_scheme="SKT"),
            "ङ्"
        )
        self.assertEqual(
            transliterate(text="aNgaH", from_scheme="SLP1", to_scheme="SKT"),
            "अङ्गः"
        )
        self.assertEqual(
            transliterate(text="jYAnam", from_scheme="SLP1", to_scheme="SKT"),
            "ज्ञानम्"
        )
        self.assertEqual(
            transliterate(text="fziH", from_scheme="SLP1", to_scheme="SKT"),
            "ऋषिः"
        )
        self.assertEqual(
            transliterate(text=".fziH", from_scheme="SLP1", to_scheme="SKT"),
            "।ऋषिः"
        )
        self.assertEqual(
            transliterate(text="kaRWakam", from_scheme="SLP1", to_scheme="SKT"),
            "कण्ठकम्"
        )
        self.assertEqual(
            transliterate(
                text="pArTAya pratiboDitAM BagavatA nArAyaRena svayam vyAsena graTitAM purARamuninA maDye mahABArate",
                from_scheme="SLP1", to_scheme="SKT"),
            "पार्थाय प्रतिबोधितां भगवता नारायणेन स्वयम् व्यासेन ग्रथितां पुराणमुनिना मध्ये महाभारते"
        )
        self.assertEqual(
            transliterate(text="rAmaH iva, 123.", from_scheme="SLP1", to_scheme="SKT"),
            "रामः इव, १२३।"
        )
        self.assertEqual(
            transliterate(text="QuRQikA'pi", from_scheme="SLP1", to_scheme="SKT"),
            "ढुण्ढिकाऽपि"
        )
        self.assertEqual(
            transliterate(text="hara hara mahAdeva", from_scheme="SLP1", to_scheme="SKT"),
            "हर हर महादेव"
        )
        self.assertEqual(
            transliterate(text="ataeva", from_scheme="SLP1", to_scheme="SKT"),
            "अतएव"
        )
        self.assertEqual(
            transliterate(text="pitFRAm kfte", from_scheme="SLP1", to_scheme="SKT"),
            "पितॄणाम् कृते"
        )
        self.assertEqual(
            transliterate(text="|.kfzRaM, vande| jagadgurum", from_scheme="SLP1", to_scheme="SKT"),
            "|।कृष्णं, वन्दे| जगद्गुरुम्"
        )
        self.assertEqual(
            transliterate(text="..kfzRaM, vande. jagadgurum.", from_scheme="SLP1", to_scheme="SKT"),
            "।।कृष्णं, वन्दे। जगद्गुरुम्।"
        )
        self.assertEqual(
            transliterate(text="ahiMsA", from_scheme="SLP1", to_scheme="SKT"),
            "अहिंसा"
        )

    def test_skt_to_slp1(self):
        self.assertEqual(
            transliterate(
                text="ङ्",
                from_scheme="SKT",
                to_scheme="SLP1"
            ),
            "N"
        )
        self.assertEqual(
            transliterate(
                text="अङ्गः",
                from_scheme="SKT",
                to_scheme="SLP1"
            ),
            "aNgaH"
        )
        self.assertEqual(
            transliterate(
                text="ज्ञानम्",
                from_scheme="SKT",
                to_scheme="SLP1"
            ),
            "jYAnam"
        )
        self.assertEqual(
            transliterate(
                text="रामः इव, १२३।",
                from_scheme="SKT",
                to_scheme="SLP1"
            ),
            "rAmaH iva, 123."
        )
        self.assertEqual(
            transliterate(
                text="कण्ठकम्",
                from_scheme="SKT",
                to_scheme="SLP1"
            ),
            "kaRWakam"
        )
        self.assertEqual(
            transliterate(
                text="ढुण्ढिकाऽपि",
                from_scheme="SKT",
                to_scheme="SLP1"
            ),
            "QuRQikA'pi"
        )
        self.assertEqual(
            transliterate(
                text="औऔ",
                from_scheme="SKT",
                to_scheme="SLP1"
            ),
            "OO"
        )
        self.assertEqual(
            transliterate(
                text="पार्थाय प्रतिबोधितां भगवता नारायणेन स्वयम् व्यासेन ग्रथितां पुराणमुनिना मध्ये महाभारते",
                from_scheme="SKT",
                to_scheme="SLP1",
            ),
            "pArTAya pratiboDitAM BagavatA nArAyaRena svayam vyAsena graTitAM purARamuninA maDye mahABArate"
        )
        self.assertEqual(
            transliterate(
                text="हर हर महादेव",
                from_scheme="SKT",
                to_scheme="SLP1"
            ),
            "hara hara mahAdeva"
        )
        self.assertEqual(
            transliterate(
                text="अतएव",
                from_scheme="SKT",
                to_scheme="SLP1"
            ),
            "ataeva"
        )
        self.assertEqual(
            transliterate(
                text="पितॄणाम् कृते",
                from_scheme="SKT",
                to_scheme="SLP1"
            ),
            "pitFRAm kfte"
        )
        self.assertEqual(
            transliterate(
                text="।.कृष्णं, वन्दे। जगद्गुरुम्",
                from_scheme="SKT",
                to_scheme="SLP1"
            ),
            "..kfzRaM, vande. jagadgurum"
        )
        self.assertEqual(
            transliterate(
                text="अहिंसा",
                from_scheme="SKT",
                to_scheme="SLP1"
            ),
            "ahiMsA"
        )
        self.assertEqual(
            transliterate(
                text="ऋषिः",
                from_scheme="SKT",
                to_scheme="SLP1"
            ),
            "fziH"
        )
        self.assertEqual(
            transliterate(
                text="।ऋषिः",
                from_scheme="SKT",
                to_scheme="SLP1"
            ),
            ".fziH"
        )

    def test_skt_to_wx(self):
        self.assertEqual(
            transliterate(
                text="ङ्",
                from_scheme="SKT",
                to_scheme="WX",
            ),
            "f"
        )
        self.assertEqual(
            transliterate(
                text="अङ्गः",
                from_scheme="SKT",
                to_scheme="WX"
            ),
            "afgaH"
        )
        self.assertEqual(
            transliterate(
                text="ज्ञानम्",
                from_scheme="SKT",
                to_scheme="WX"
            ),
            "jFAnam"
        )
        self.assertEqual(
            transliterate(
                text="पार्थाय प्रतिबोधितां भगवता नारायणेन स्वयम् व्यासेन ग्रथितां पुराणमुनिना मध्ये महाभारते",
                from_scheme="SKT",
                to_scheme="WX"
            ),
            "pArWAya prawiboXiwAM BagavawA nArAyaNena svayam vyAsena graWiwAM purANamuninA maXye mahABArawe"
        )
        self.assertEqual(
            transliterate(
                text="रामः इव, १२३।",
                from_scheme="SKT",
                to_scheme="WX"
            ),
            "rAmaH iva, 123."
        )
        self.assertEqual(
            transliterate(
                text="कण्ठकम्",
                from_scheme="SKT",
                to_scheme="WX"
            ),
            "kaNTakam"
        )
        self.assertEqual(
            transliterate(
                text="ढुण्ढिकाऽपि",
                from_scheme="SKT",
                to_scheme="WX"
            ),
            "DuNDikAZpi"
        )
        self.assertEqual(
            transliterate(
                text="औऔ",
                from_scheme="SKT",
                to_scheme="WX"
            ),
            "OO"
        )
        self.assertEqual(
            transliterate(
                text="हर हर महादेव",
                from_scheme="SKT",
                to_scheme="WX"
            ),
            "hara hara mahAxeva"
        )
        self.assertEqual(
            transliterate(
                text="अतएव",
                from_scheme="SKT",
                to_scheme="WX"
            ),
            "awaeva"
        )
        self.assertEqual(
            transliterate(
                text="पितॄणाम् कृते",
                from_scheme="SKT",
                to_scheme="WX"
            ),
            "piwQNAm kqwe"
        )
        self.assertEqual(
            transliterate(
                text="।.कृष्णं, वन्दे। जगद्गुरुम्",
                from_scheme="SKT",
                to_scheme="WX"
            ),
            "..kqRNaM, vanxe. jagaxgurum"
        )
        self.assertEqual(
            transliterate(
                text="अहिंसा",
                from_scheme="SKT",
                to_scheme="WX"
            ),
            "ahiMsA"
        )
        self.assertEqual(
            transliterate(
                text="ऋषिः",
                from_scheme="SKT",
                to_scheme="WX"
            ),
            "qRiH"
        )
        self.assertEqual(
            transliterate(
                text="।ऋषिः",
                from_scheme="SKT",
                to_scheme="WX"
            ),
            ".qRiH"
        )


if __name__ == '__main__':
    unittest.main()
