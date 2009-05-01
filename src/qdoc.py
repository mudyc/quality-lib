# Matti Katila, 2009

import sys
import docutils
from docutils import readers, io, parsers, frontend, core

def usage():
    print "qdoc - Quality library tool"
    print "Usage: python qdoc.py DESTINATION SOURCE.."

if __name__ == '__main__':
    if len(sys.argv) <= 2:
        print 'Error: not enough parameters given.\n'
        usage()
        sys.exit(1)

    documents = []
    for file in sys.argv[2:]:
        print 'Reading', file


        reader=None
        reader_name='standalone'
        parser=None
        parser_name='restructuredtext'
        writer=None
        writer_name='pseudoxml'
        settings=None
        settings_spec=None
        settings_overrides=None
        config_section=None


        pub = core.Publisher(reader, parser, writer, settings=settings)
        pub.set_components(reader_name, parser_name, writer_name)
        opts = pub.setup_option_parser()
        pub.settings = opts.parse_args(None)
        pub.set_io(file)
        document = pub.reader.read(pub.source, pub.parser,
                                   pub.settings)

        print document.pformat()
        #self.apply_transforms()
        #output = self.writer.write(self.document, self.destination)
