---
layout: post
title:  "Let&#39;s Make a Language: C♭ - Part 4"
tags:   C♭, language design, compilers

synopsis: In which I implement &quot;Declarations MUST use the var keyword.&quot;.
---

# {{ page.title }}

{{ page.synopsis }}
{: .subtitle }

-----

**Note:** When I write "declarations must use the var ``var`` keyword," I
really mean variable declarations local to a method or at the global level.

I haven't talked about C♭ in more than a month. Time to implement another
story. This one requires us to check if assignments use the ``var`` keyword
rather than an actual type. That sounds great!

Because I'm writing a transcompiler, I don't have to be so strict about the
rules. It does mean, though, that I have more test cases since I won't build
a full abstract syntax tree. With a full abstract syntax tree, I could
inspect every portion of the program to ensure that it meets the lexical and
syntactic rules set forth by the language's specification. Since I've gone the
cheap route, I'll have to act more meticulously with my tests.

## Test Cases

The C♭ transcompiler should interpret each of the following inputs to the
associated output regardless of whitespace. With that in mind, I will run each
string through the parser three times. The first run will evaluate the test
input as-is. The second run will evaluate it with all line breaks removed.
Finally, the last run will evaulate it with all sequences of white-space
replaced with a single space.

{% highlight csharp %}
// criterion-compliant strings
var global = "var \n globalVariable \n = \n 7;"
var method = "class Foo() {\n" +
             "  public void DoSomething(string moo) {\n" +
             "    var moreMoo = moo + \"moo\";\n" +
             "  }\n" +
             "  private string foo = \"goo\";\n" +
             "}";

// criterion-violating strings
var globalBad = "int \n globalVariable \n = \n 7;"
var methodBad = "class Foo() {\n" +
                "  public void DoSomething(string moo) {\n" +
                "   string moreMoo = moo + \"moo\";\n" +
                "  }\n" +
                "  private string foo = \"goo\";\n" +
                "}";
{% endhighlight %}

With those in place in the test file, I can start with the lexer/parser work.

## Analysis

We need to identify partial statements of the form

> ``type_declaration variable_name '='``

and ignore partial statements of the form

> ``visibility_modifier type_declaration variable_name '='``

where ``variable_name`` and ``type_declaration`` are any string that does not
contain a space, and ``visibility modifier`` can have any of the following
values.

* public
* internal
* protected
* protected internal
* private

Currently, I have only the ``NOT_LONG_ENOUGH`` token defined. It looks like I
need two new tokens for the lexer to provide to the parser.

__VISIBILITY_MODIFIER__
: This token will indicate of the values from the above list.

__IDENTIFIER__
: This token will indicate a string of non-space characters.

Since C♭ acts as a transcompiler, I can let the C# compiler decide that it 
has valid identifiers.

## Lexer work

In the parser, I define the two new tokens. Since I have to examine the value
of the token for ``type_declaration``, I need to make sure that the lexer can
pass that value to the parser. To that end, I modify the ``%union`` and
``%token`` declarations in "parser.y" to the following:

{% highlight csharp %}
%union {
  public int integer;
  public string str;                // New line
}

%token<integer> NOT_LONG_ENOUGH
%token<str> IDENTIFIER              // New line
%token VISIBILITY_MODIFIER          // New line
{% endhighlight %}

In the lexer I can now put those to use. When I come across values that should
match either of those tokens or the equals sign, I will pass those back to the
parser for matching.

{% highlight csharp %}
%namespace cflat

VISIBILITY    (public|protected|internal|protected\s+internal|private)
IDENTIFIER    [a-zA-Z_][a-zA-Z0-9_]*

%{
private int totalLines = 0;
%}

%%

{VISIBILITY}    { return (int) Tokens.VISIBILITY_MODIFIER; }
{IDENTIFIER}    { yylval.str = yytext; return (int) Tokens.IDENTIFIER; }
'='             { return (int) yytext[0]; }

\n              { totalLines += 1; }
<<EOF>>         {
                  yylval.integer = totalLines;
                  if(totalLines < 300) return (int) Tokens.NOT_LONG_ENOUGH;
                  else return (int) Tokens.EOF;
                }{% endhighlight %}

## Parser work

Now that the lexer will return the new tokens, I want the parser to take
advantage of them.
