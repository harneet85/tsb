from ansi2html import Ansi2HTMLConverter
conv = Ansi2HTMLConverter()
ansi = "".join(sys.stdin.readlines())
html = conv.convert(ansi)
