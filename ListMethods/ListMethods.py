import traceback
methodSignature = '(public|protected|private|static|\s) +[\w\<\>\[\]]+\s+(\w+) *\([^\)]*\) *(\{?|[^;])'


def main():
    import getopt
    import sys
    import re
    try:
        options, args = getopt.getopt(sys.argv[1:], 'i:h', ['input=', 'help'])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like 'option -a not recognized'
        sys.exit(2)

    javaFile = ''
    # read args
    for opt, arg in options:
        if opt in ('-i', '--input'):
            javaFile = arg

    if javaFile is '':
        javaFile = sys.argv[1]

    try:
        with open(javaFile, "rU") as file:
            lines = file.readlines()
            print '//', javaFile
            print '//', len(lines), 'lines of code'
            methods = {}
            for line in lines:
                try:
                    m = re.search(methodSignature, line)
                    if len(m.group(0)) > 0:
                        methodLine = m.group(0)
                        methodLine = methodLine.replace(' {', '')
                        access, type, methodSig = methodLine.split(' ', 2)
                        # print m.group(0)
                        methods[methodSig] = (access, type)
                except:
                    a = 1
            # print '\nSorted list\n'

            for methodSig in sorted(methods.keys()):
                (access, type) = methods[methodSig]
                print '{} {} {};'.format(access, type, methodSig)
    except Exception, e:
        traceback.print_exc()


if __name__ == '__main__':
    main()
