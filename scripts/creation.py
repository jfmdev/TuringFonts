
# Load module
import fontforge

# Get the font to be modified
myFont = fontforge.open("C:\MyFonts\Arial.ttf")

# Define the text and plain alphabets to use
plain = "abcdefghijklmnopqrstuvwxyz"
cipher = "zyxwvutsrqponmlkjihgfedcba"

# Define the name of the new font.
newFontName = myFont.fontname + "-" + cipher

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
