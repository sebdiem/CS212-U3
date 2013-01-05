## Unit 3 Homework: parse/convert str regular expression to API

import grammar_engine

#ONEOF => ([^\\b\\f\\r\\n\\t\"\\\\[\]]|\\\[\"\\\/\\b\\f\\r\\n\\t]|u[0-9a-fA-F]{4})*
REGRAMMAR = grammar_engine.grammar("""RE =>  [[] ONEOF []] | LIT
ONEOF => [^\[\]]*
ALT => [^|] | ALT |
LIT => ([^\\b\\f\\r\\n\\t\"\\\]|\\\[\"\\\/\\b\\f\\r\\n\\t]|u[0-9a-fA-F]{4})""", whitespace='')

def parse_re(pattern):
	return (grammar_engine.parse('RE', pattern, REGRAMMAR))

print "########## parse : "+str(parse_re("[abc]"))

def convert(tree):
	pass

def lit(s): return lambda t: set([t[len(s):]]) if t.startswith(s) else null
def seq(x, y): return lambda t: set().union(*map(y, x(t)))
def alt(x, y): return lambda t: x(t) | y(t)
def oneof(chars): return lambda t: set([t[1:]]) if (t and t[0] in chars) else null
dot = lambda t: set([t[1:]]) if t else null
eol = lambda t: set(['']) if t == '' else null
def star(x): return lambda t: (set([t]) | 
                               set(t2 for t1 in x(t) if t1 != t
                                   for t2 in star(x)(t1)))

null = frozenset([])
 
