> **Notice:** this project has been archived for being considered feature complete.

Turing fonts
============

_Publish uncrawable and uncopiable texts_

**TuringFonts** is a simple technique for generate content (for websites or PDF files) that can't we crawled by bots or copied using the clipboard.

It's useful in situations in which you want to publish some sensitive content that you don't want to be indexed by search engines like Google or Bing (such as e-mail addresses, telephone numbers or personal names) or when you don't want to allow the user to _copy and paste_ your text (to avoid plagiarism or unauthorized modifications).

## How it works?

This technique is based on the [simple substitution cipher](http://en.wikipedia.org/wiki/Substitution_cipher#Simple_substitution) method and in the use of custom fonts.

> The simple substitutions cipher in a method of encoding in which each letter is replaced by another one. 
>For example, you could decide to replace each letter by his neighbour in the alphabet (write 'b' instead of 'a', 'c' instead of 'b', etc.), in that case the text "Hello" would be write as "Ifmmp".

>A font (in computing) is basically a file that indicates how to draw each letter. So, for example, some fonts define that the letter 'O' must be draw rounded while others indicate that must be oval.

So basically you encrypt your text using some substitution cipher and then you apply (to that text) a _Turing font_ that inverses the substitution previously made.

>A Turing font is a font whose symbols has been unordered on purpose. So when a letter is found, another letter is draw in his place. For example, a Turing font may indicate to draw an 'a' when encountering a 'b', draw a 'b' when encountering a 'c', etc.).

In that's way any bot or computer, that get access to your website or PDF file, is going to read the encrypted text while all humans visitors are going to read the original text.

[Click here to see a live demo](http://jfmdev.github.io/TuringFonts/index.html#demo)

## How to use it

In order to use this technique, you must follow a two step process:

1. Encode you text using some substitution method. You can use [this encoder](http://jfmdev.github.io/TuringFonts/encoder.html) to do it.

2. Apply, to the previous text, a Turing font. In the [download section](http://jfmdev.github.io/TuringFonts/index.html#downloads) you can find a list of fonts ready to be used.

If you want to use your own substitution alphabets and/or generate your own Turing fonts, I recommend you to [read the documentation](http://jfmdev.github.io/TuringFonts/advanced.html)

## License

All fonts, scripts and content of this work are licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/ "CC BY-SA 4.0").

![CC BY-SA 4.0](https://i.creativecommons.org/l/by-sa/4.0/88x31.png "CC BY-SA 4.0")
