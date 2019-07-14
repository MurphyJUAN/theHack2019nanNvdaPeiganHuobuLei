import re
from collections import defaultdict, Counter

def bold(txt):
    return '\x1b[1m%s\x1b[0m' % txt

DATA = [
    {
        'title': 'Django',
        'description': 'Django is a high-level Python Web framework that '
            'encourages rapid development and clean, pragmatic design.  Built by '
            'experienced developers, it takes care of much of the hassle of Web '
            'development, so you can focus on writing your app without needing to '
            'reinvent the wheel. It’s free and open source.'
    },
    {
        'title': 'Python',
        'description': 'Python is a programming language that lets you work '
            'more quickly and integrate your systems more effectively.'
    },
]

SPLIT_RE = re.compile(r'[^a-zA-Z0-9]')
def tokenize(text):
    yield from SPLIT_RE.split(text)

def text_only(tokens):
    for t in tokens:
        if t.isalnum():
            yield t

def lowercase(tokens):
    for t in tokens:
        yield t.lower()

def stem(tokens):
    for t in tokens:
        if t.endswith('ly'):
            t = t[:-2]
        yield t

SYNONYMS = {
    'rapid': 'quick',
}
def synonyms(tokens):
    for t in tokens:
        yield SYNONYMS.get(t, t)

def analyze(text):
    tokens = tokenize(text)
    for token_filter in (text_only, lowercase, stem, synonyms):
        tokens = token_filter(tokens)
    yield from tokens

def index_docs(docs, *fields):
    index = defaultdict(lambda: defaultdict(Counter))
    for id, doc in enumerate(docs):
        for field in fields:
            for token in analyze(doc[field]):
                index[field][token][id] += 1
    return index

def combine_and(*args):
    if not args:
        return Counter()
    out = args[0].copy()
    for c in args[1:]:
        for doc_id in list(out):
            if doc_id not in c:
                del out[doc_id]
            else:
                out[doc_id] += c[doc_id]
    return out

def combine_or(*args):
    if not args:
        return Counter()
    out = args[0].copy()
    for c in args[1:]:
        out.update(c)
    return out

COMBINE = {
    'OR': combine_or,
    'AND': combine_and,
}

def search_in_fields(index, query, fields):
    for t in analyze(query):
        yield COMBINE['OR'](*(index[f][t] for f in fields))

def search(index, query, operator='AND', fields=None):
    combine = COMBINE[operator]
    return combine(*(search_in_fields(index, query, fields or index.keys())))

def query(index, query, operator='AND', fields=None):
    print('Search for "%s" using %s in %s' % (bold(query), bold(operator), fields or 'all fields'))
    print('-'*80)
    ids = search(index, query, operator, fields)
    for doc_id, score in ids.most_common():
        print('%s found with score of %s' % (bold(DATA[doc_id]['title']), bold(score)))
    print('\n')

index = index_docs(DATA, 'title', 'description')
query(index, 'Python')
query(index, 'Python', fields=['title'])
query(index, 'python', fields=['description'])
query(index, 'Python web')
query(index, 'Python web', 'OR')
query(index, 'quick')
query(index, 'rapid')
query(index, 'of')