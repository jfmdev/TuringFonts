# Load module
import fontforge

def generateTuringFont(myFont, cipher, newFontName):
	plain = "abcdefghijklmnopqrstuvwxyz"
	
	# Create a font to use as auxiliar variable
	temporal = fontforge.font()
		
	# Change the order of the letters
	plain = plain + plain.upper()
	cipher = cipher + cipher.upper()
	for i in range(len(plain)):
		myFont.selection.select( plain[i] )
		myFont.copy()                                   
		temporal.selection.select( cipher[i] )
		temporal.paste()

	# Copy back the letters in the auxiliar font to the original font.
	temporal.selection.select(("ranges",None),"a","z")
	myFont.selection.select(("ranges",None),"a","z")
	temporal.copy()
	myFont.paste()
	temporal.selection.select(("ranges",None),"A","Z")
	myFont.selection.select(("ranges",None),"A","Z")
	temporal.copy()
	myFont.paste()

	# Save new font
	myFont.fontname = newFontName
	myFont.familyname = newFontName
	myFont.fullname = newFontName
	myFont.save(newFontName + ".sfd")
	temporal.close()

generateTuringFont(fontforge.open("C:\MyFonts\Arial.ttf"), "zyxwvutsrqponmlkjihgfedcba", "Arial_Atbash")
generateTuringFont(fontforge.open("C:\MyFonts\Verdana.ttf"), "zyxwvutsrqponmlkjihgfedcba", "Verdana_Atbash")
generateTuringFont(fontforge.open("C:\MyFonts\Courier New.ttf"), "zyxwvutsrqponmlkjihgfedcba", "CourierNew_Atbash")
generateTuringFont(fontforge.open("C:\MyFonts\Tahoma.ttf"), "zyxwvutsrqponmlkjihgfedcba", "Tahoma_Atbash")
generateTuringFont(fontforge.open("C:\MyFonts\Georgia.ttf"), "zyxwvutsrqponmlkjihgfedcba", "Georgia_Atbash")
