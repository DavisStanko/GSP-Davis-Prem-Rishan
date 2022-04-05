import sys
if sys.version_info.major == 3:
    import tkinter as tk, tkinter.font as tk_font
else:
    import Tkinter as tk, tkFont as tk_font
root = tk.Tk()
print(tk_font.families())
print(tk_font.names())

fonts = ['Academy Engraved LET', 'Al Bayan', 'Al Nile', 'Al Tarikh', 'American Typewriter', 'Andale Mono', 'Apple '
                                                                                                           'Braille',
         'Apple Chancery', 'Apple Color Emoji', 'Apple SD Gothic Neo', 'Apple Symbols', 'AppleGothic',
         'AppleMyungjo', 'Arial', 'Arial Black', 'Arial Hebrew', 'Arial Hebrew Scholar', 'Arial Narrow',
         'Arial Rounded MT Bold', 'Arial Unicode MS', 'Avenir', 'Avenir Next', 'Avenir Next Condensed', 'Ayuthaya',
         'Baghdad', 'Bangla MN', 'Bangla Sangam MN', 'Baskerville', 'Beirut', 'Big Caslon', 'Bodoni 72', 'Bodoni 72 '
                                                                                                         'Oldstyle',
         'Bodoni 72 Smallcaps', 'Bodoni Ornaments', 'Bradley Hand', 'Brush Script MT', 'Chalkboard', 'Chalkboard SE',
         'Chalkduster', 'Charter', 'Cochin', 'Comic Sans MS', 'Copperplate', 'Corsiva Hebrew', 'Courier',
         'Courier New', 'Damascus', 'DecoType Naskh', 'Devanagari MT', 'Devanagari Sangam MN', 'Didot',
         'DIN Alternate', 'DIN Condensed', 'Diwan Kufi', 'Diwan Thuluth', 'Euphemia UCAS', 'Farah', 'Farisi',
         'Futura', 'Galvji', 'GB18030 Bitmap', 'Geeza Pro', 'Geneva', 'Georgia', 'Gill Sans', 'Grantha Sangam MN',
         'Gujarati MT', 'Gujarati Sangam MN', 'Gurmukhi MN', 'Gurmukhi MT', 'Gurmukhi Sangam MN', 'Heiti SC',
         'Heiti TC', 'Helvetica', 'Helvetica Neue', 'Herculanum', 'Hiragino Maru Gothic ProN', 'Hiragino Mincho '
                                                                                               'ProN',
         'Hiragino Sans', 'Hiragino Sans GB', 'Hoefler Text', 'Impact', 'InaiMathi', 'ITF Devanagari',
         'ITF Devanagari Marathi', 'Kailasa', 'Kannada MN', 'Kannada Sangam MN', 'Kefa', 'Khmer MN', 'Khmer Sangam '
                                                                                                     'MN',
         'Kohinoor Bangla', 'Kohinoor Devanagari', 'Kohinoor Gujarati', 'Kohinoor Telugu', 'Kokonor', 'Krungthep',
         'KufiStandardGK', 'Lao MN', 'Lao Sangam MN', 'LiSong Pro', 'Lucida Grande', 'Luminari', 'Malayalam MN',
         'Malayalam Sangam MN', 'Marker Felt', 'Menlo', 'Microsoft Sans Serif', 'Mishafi', 'Mishafi Gold', 'Monaco',
         'Mshtakan', 'Mukta Mahee', 'Muna', 'Myanmar MN', 'Myanmar Sangam MN', 'Nadeem', 'New Peninim MT',
         'Noteworthy', 'Noto Nastaliq Urdu', 'Noto Sans Kannada', 'Noto Sans Myanmar', 'Noto Sans Oriya', 'Noto Serif '
                                                                                                          'Myanmar',
         'Optima', 'Oriya MN', 'Oriya Sangam MN', 'Palatino', 'Papyrus', 'Party LET', 'Phosphate', 'PingFang HK',
         'PingFang SC', 'PingFang TC', 'Plantagenet Cherokee', 'PT Mono', 'PT Sans', 'PT Sans Caption',
         'PT Sans Narrow', 'PT Serif', 'PT Serif Caption', 'Raanana', 'Rockwell', 'Sana', 'Sathu', 'Savoye LET',
         'Shree Devanagari 714', 'SignPainter', 'Silom', 'Sinhala MN', 'Sinhala Sangam MN', 'Skia',
         'Snell Roundhand', 'Songti SC', 'Songti TC', 'STIXGeneral', 'STIXIntegralsD', 'STIXIntegralsSm',
         'STIXIntegralsUp', 'STIXIntegralsUpD', 'STIXIntegralsUpSm', 'STIXNonUnicode', 'STIXSizeFiveSym',
         'STIXSizeFourSym', 'STIXSizeOneSym', 'STIXSizeThreeSym', 'STIXSizeTwoSym', 'STIXVariants', 'STSong',
         'Sukhumvit Set', 'Symbol', 'Tahoma', 'Tamil MN', 'Tamil Sangam MN', 'Telugu MN', 'Telugu Sangam MN',
         'Thonburi', 'Times', 'Times New Roman', 'Trattatello', 'Trebuchet MS', 'Verdana', 'Waseem', 'Webdings',
         'Wingdings', 'Wingdings 2', 'Wingdings 3', 'Yuanti SC', 'Yuanti TC', 'Zapf Dingbats', 'Zapfino']
