from nose.tools import*
from ex48_lexicon import parser

def test_parse_sentence():
    subject = ('noun', 'princess')
    verb = ('verb', 'kill')
    object = ('noun', 'bear')
    list_from_lexicon = [subject, verb, object]
    test = parser.parse_sentence(list_from_lexicon)
    assert_equal(test.__str__(), "princess kill bear" )


def test_skip():
    assert_equal(parser.skip([('type is same', 'skipped/popped word')], 'type is same'), None)
    assert_equal(parser.skip([('type a', 'un-popped word')], 'type b'), None)


def test_peek():
    assert_equal(parser.peek([('just', 'some'),
                              ('list', 'of'),
                              ('tuple', 'pair')]),
                 'just')


def test_match():
    assert_equal(parser.match([('expecting type', 'of words')], 'expecting type'),
                 ('expecting type', 'of words'))


def test_parse_subject():
    assert_equal(parser.parse_subject([('noun', 'common name')]), ('noun', 'common name'))
    assert_equal(parser.parse_subject([('verb', 'go')]), ('noun', 'player'))
    assert_raises(parser.ParserError, parser.parse_subject, [('direction', 'north')])
    assert_raises(parser.ParserError, msg='Expected a verb next.')


def test_parse_verb():
    assert_equal(parser.parse_verb([('verb', 'go')]), ('verb', 'go'))
    assert_raises(parser.ParserError, parser.parse_verb, [('noun', 'common name')])
    assert_raises(parser.ParserError, parser.parse_verb, [('direction', 'north')])
    assert_raises(parser.ParserError, msg='Expected a verb next.')

def test_parse_object():
    assert_equal(parser.parse_object([('noun', 'common name')]), ('noun', 'common name'))
    assert_equal(parser.parse_object([('direction', 'north')]), ('direction', 'north'))
    assert_raises(parser.ParserError, parser.parse_object, [('verb', 'go')])
    assert_raises(parser.ParserError, msg="Expected a noun or direction next.")


@raises(parser.ParserError)
def test_parser_error():
    raise parser.ParserError()
