import sys
import markdown


src = sys.argv[1]
dst = sys.argv[2]

with open(src, 'r') as srcf:
    with open(dst, 'w') as file:
        file.write(markdown.markdown(srcf.read()))
