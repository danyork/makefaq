#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# -------------------------------------------------------------
#
# makefaq.py
# Revision:  2.6
# Rev Date:  ?? <month> 2009
#
# This program is designed to take a text file and generate
# a single-page formatted Frequently-Asked-Question file.
#
# It reads in FAQ categories, questions and answers from (by default)
# a file called "faq.dat", adds an HTML header and footer, and
# writes the information to "faq.html".  There is also the 
# ability to write out a text version.
#
# See the "Notes" section below for more details.
#
# If you have any comments about this script, of if you make
# an improved version, please contact Dan York at 
# dyork@lodestar2.com
#
# Copyright (c) 1999-2009 Dan York, dyork@Lodestar2.com
# http://www.Lodestar2.com/software/makefaq/ or
# http://www.makefaq.org/
#
# The author acknowledges significant contributions to the
# code by Dave Seidel (dave@superluminal.com) and he can
# definitely be considered as the co-author of this code.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or any later version.
#
# This program is distributed in the hope that it will be useful
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the 
# GNU General Public License for more details.
# http://www.gnu.org/copyleft/gpl.html
#
# -------------------------------------------------------------
#
# If you use this program to generate a FAQ page for a public
# web site, please do send the URL to dyork@lodestar2.com so
# that your FAQ can be listed on the home page for makefaq as
# another example.
#
# -------------------------------------------------------------
#
# LANGUAGE LOCALIZATION ISSUES
#
# If you do not have the LANG environment variable set, you will need to
# set your locale here or use the '-L' command-line option. 
# CURRENTLY SUPPORTED values are:
#
# 'de_DE' (German)
# 'en_US' (US English)
# 'fr_FR' (French) 
# 'pt_BR' (Brazilian Portugeuse) 
#
# This affects the dates, 'FAQ Revised' and "Table of Contents" strings.
#
# If you do not set a LANG or use '-L', you will receive the 'en_US'
# settings.

LOCALE = "en_US"

# If you would like to add support for your language, first determine the
# appropriate POSIX locale code and then add the appropriate messages to
# the "LocalizeStrings" function below. If your LOCALE is not a valid code,
# makefaq will print a error message and use the 'en_US' settings instead.

# If for some reason you want to ignore the LANG environment variable and
# force it to use a specific locale, use the '-L' command-line option.
# (Note that this *is* case-sensitive.)

#
# NOTE TO USERS ON NON-LINUX PLATFORMS: It appears that current versions of
# the locale module supplied with Python on at least Windows, HP-UX and 
# FreeBSD 4.x do not allow the operating system locale to be set. Because
# of this, the exact format of the date/time stamp may not be localized to
# the conventions of your locale.  Other than that, however, the program
# will work fine and, if you are using one of the locales mentioned above,
# the appropriate text strings *will* be printed out.
#

# -------------------------------------------------------------
# NOTES
#
# This program is made available purely so that others might 
# be saved the frustration of building FAQ pages by hand.  
# Examples of its use can be found at:
#
#   http://www.makefaq.org/faq.html
#
# The input file is called "faq.dat" by default (but can be changed
# by command-line options). It uses an XML-ish language in the data 
# file to delimit the three items: category of the question, question
# text and answer text. An example would be:
#
#  <c>General
#  <q>What is the meaning of life?
#  <a>I have <i>no</i> idea!
#
# The Question and Answer sections can include HTML, as shown above.
# The category, question and answer can all be on one line, or can be
# on separate lines.  The <c>, <q>, and <a> delimiters can be on the
# same line as their text, as shown above, or can be on a line of
# their own. Unlike true XML, there are no end tags. See the sample 
# 'faq.dat' provided with the program for examples of data file layout.
#
# In the directory where the script is run, there must be three
# files (in the default configuration):
#
# - faq.dat         - the text file with the questions and answers
# - faqheader.html  - an HTML file with the top of the file
# - faqfooter.html  - an HTML file with the bottom of the file
#
# Sample files should have been provided with this code.
#
# Please read the accompanying "ChangeLog" file to understand
# the substantial changes that have been made to the code base.
#
# Also please look at the README file before using this script.
#
# -------------------------------------------------------------
# BUGS
#
# If special entities like &lt; and &gt; are used in faq.dat to 
# give a < and > sign, they are NOT stripped in the text or screen
# output.
#
# -------------------------------------------------------------
# REVISION HISTORY
#
# ?? ??? 2009 - 2.6 ...
#
# 29 Feb 2004 - 2.5 released with PEP-263 definition of source code
#                encoding so that python 2.3 will not generate warnings
# 11 Nov 2002 - 2.4 released with ability to export to DocBook XML
#                and the '-N' command-line option to suppress numbering
# 10 Aug 2002 - 2.3 released with '-j' command-line option and CSS
#                support
# 13 Jul 2001 - 2.2 released with bug fix so it will run on non-Linux
#               operating systems
# 22 Apr 2001 - 2.1 released with minor bug fix and Portuguese lang info
#  2 Apr 2001 - 2.0 released with multi-line datafile format
# 24 Mar 2001 - 0.5 released with '-d' command-line option
# 22 Feb 2000 - 0.4 uploaded with fix to data sorting problem
#  8 Feb 2000 - 0.3.1 uploaded with minor bug fix
# 22 Jan 2000 - 0.3 uploaded after substantantial modifications
#               by Dave Seidel (dave@superluminal.com)
# 14 Jan 2000 - (dave) added command line processing, error handling,
#               comments
# 13 Jan 2000 - (dave) submitted to BEAST project
#  3 Jan 2000 - 0.2 uploaded in beta state to web site
#
# -------------------------------------------------------------
# QUICK SUMMARY OF CHANGES TO VERSION 2.6
#
# <text here>
#
# -------------------------------------------------------------
# QUICK SUMMARY OF CHANGES TO VERSION 2.5
#
# Purely a bug fix version so that users with python 2.3 will no
# longer see a warning about missing source code encoding.
#
# -------------------------------------------------------------
# QUICK SUMMARY OF CHANGES TO VERSION 2.4
#
# See the accompanying "ChangeLog" file for full details.
#
# New features:
#   - There is now the ability to generate a DocBook XML <qandaset>
#       file which could then be processed using XSLT tools into a
#       PDF file or other format (including HTML).  Usage is through
#       the "DocBookXML" config that was added, as in:
#
#       ./makefaq.py -c DocBookXML
#
#       plus whatever other command-line options are desired. The 
#       default output file for this config is "faq-output.xml".
#
#       Note that the contents of the question and answer tags are
#       simply copied to the output XML file, so if they contain
#       HTML tags, those will be copied over, and would then make
#       the resulting XML file no longer valid.
#
#   - A "-N" command-line option was added that will suppress 
#       numbering of questions and answers.  This was desirable for
#       the DocBook XML generation as the standard DocBook XSLT 
#       stylesheets can provide numbering for FAQ entries.
#
#   - The attribute "self.createTOC" was added to the DefaultConfig
#       and is set to TRUE so that a TOC will be generated by default.
#       However, this can be overridden in subclassed configs in
#       order to suppress the creation of a TOC by setting the value
#       to FALSE.  As an example, this was done in the DocBookXMLConfig.
#
# Updates:
#   - German strings updated (Fabian Melzow)
#   - Portugeuse strings updated (Mauro Persano)
#
# -------------------------------------------------------------
# ACKNOWLEDGEMENTS
#
# Beyond Dave Seidel, the following people need to be acknowledged
# for their assistance either with direct code or with ideas that led
# me to the right code. The version number in which their contributions 
# was first incorporated is in parentheses after their name.
#
# - Guy Brand for the suggestion to use the locale module and
#      the strftime function for localization, also for the
#      French phrases (2.0)
# - Nicolas Devillard for his multi-line entry implementation (2.0)
# - Wolfgang Ocker for one multi-line entry implementation and for
#      his implementation with gettext (both of which were very useful
#      in trying to figure out how to implement both features in 2.0)
# - Wolfgang Ocker and Lenz Grimmer for the German phrases (2.0)
# - César A. K. Grossmann for his Portugeuse phrases (2.1)
# - Michael Wiedmann for catching the PrintTimeStamp bug (2.1) and
#      also for packaging makefaq as a Debian package (from 2.0 on)
# - Michael Wiedmann for the man page (2.1)
# - Jerry (??) and Ken Ito for identifying the PrintTimeStamp setlocale
#      issue on non-Linux platforms and Gareth Noyce for verifying the 
#      problem (2.2)
# - Fabian Melzow for the German JumpString translation (2.4)
# - Bernhard Reiter for the suggestion to move comments about functions
#      into actual python docstrings (2.4)
# - Mauro Persano for the Portugeuse JumpString translation (2.4)
# - Kenzaburo Ito for his URL for the Mantis FAQ (2.4)
#
# See also the CREDITS file included with the source code.
#
# -------------------------------------------------------------

import getopt
import locale
import os
from sys    import argv, stdout, stderr, exit
from time   import asctime, localtime, time, strftime
from string import strip, split, atoi
from re     import sub

TRUE  = 1
FALSE = 0

def TellTruth(thing):
   """Simple function to return either true or false."""
   if thing:
      return 'TRUE'
   return 'FALSE'

def LocalizeStrings(cfg,lc):
    """ These are the strings that are printed for the "FAQ Revised" and
         "Table of Contents" strings in the output file.
         IF YOU WOULD LIKE TO ADD ANOTHER LANGUAGE, copy the three lines for
         one of the entries beginning with 'elif' and modify them to have your
         locale code and appropriate messages. PLEASE SEND ANY ADDITIONS TO ME
         at 'dyork@Lodestar2.com' so that I can incorporate them into future 
         versions of the program. """

    if lc == 'fr_FR':
       cfg.RevString = 'Dernière révision:'
       cfg.TOCString = 'Table des matières'
       cfg.JumpString = 'Return to top of page'

    elif lc == 'de_DE':
       cfg.RevString = 'FAQ überarbeitet am:'
       cfg.TOCString = 'Inhalt'
       cfg.JumpString ='Zurück zum Seitenanfang'
    
    elif lc == 'pt_BR':
       cfg.RevString = 'FAQ Revisado em:'
       cfg.TOCString = 'Tabela de Conteúdo'
       cfg.JumpString = 'Voltar ao topo da página'
       # Note that the a with an acute accent should be &aacute; in HTML
    
    # ADD NEW LOCALES HERE. THEY MUST BE BEFORE THE 'else:' statement below.
    # Note that indentation *is* significant in python and your 'elif' statement
    # needs to line up with the other ones.  You can remove the comment 
    # characters from the lines below and use it if you wish.

    #elif lc == 'de_DE':
    #   cfg.RevString = 'FAQ Revised:'
    #   cfg.TOCString = 'Inhalt'
    #   cfg.JumpString ='Zurück zum Seitenanfang'
   
    # If no locale matches, default to US English
    else:
       cfg.RevString = 'FAQ Revised:'
       cfg.TOCString = 'Table of Contents'
       cfg.JumpString = 'Return to top of page'
        

# -------------------------------------------------------------

class DefaultConfig:
   """
   Base configuration class, with all filename and formatting
   defaults; note that all the data defined in this class
   is inherited by its subclasses, unless you override it
   """
   def show(self):
      print '  Configuration: ' + self.name     + '\n' + \
            '     Input file: ' + self.infile   + '\n' + \
            '    Header file: ' + self.headfile + '\n' + \
            '    Footer file: ' + self.footfile + '\n' + \
            '    Output file: ' + self.outfile  + '\n' + \
            'Old-style Delimiter: ' + self.delimiter  + '\n' + \
            ' Cat  Delimiter: ' + self.cdelim  + '\n' + \
            '   Q  Delimiter: ' + self.qdelim  + '\n' + \
            '   A  Delimiter: ' + self.adelim  + '\n' + \
	    '       addJumps: ' + TellTruth(self.addJumps) + '\n' + \
	    '      createTOC: ' + TellTruth(self.createTOC) + '\n' + \
	    'numberQuestions: ' + TellTruth(self.numberQuestions) + '\n' + \
            '       hasLinks: ' + TellTruth(self.hasLinks)

   def __repr__(self):
      return self.name;

   def __init__(self):
      # name
      self.name = "default"

      # if this is FALSE, we strip and/or transform
      # HTML tags; see the function FixSpecialText below
      self.hasLinks = TRUE

      # is a TOC created?  In most cases, the answer will be true,
      # but in some cases, such as DocBook output, we want to 
      # suppress creation of a TOC
      self.createTOC = TRUE

      # Are the categories and questions numbered? Default is yes.
      self.numberQuestions = TRUE

      # default filenames
      self.headfile = 'faqheader.html'
      self.footfile = 'faqfooter.html'
      self.infile   = 'faq.dat'

      # If you want the default behaviour of makefaq 0.2, 
      # which was to dump the output to stdout, change the outfile
      # line to:
      #
      # self.outfile  = 'STDOUT'
      #
      self.outfile  = 'faq.html'

      #
      # Set a flag in the default configuration that it uses the most 
      # current XML format.  This allows for this
      # to be overwritten in another config.
      #
      # The numbers are input on the command line in conjunction with
      # the "-r" flag. For instance, you can use "-r 1" to use the
      # original flat file or "-r 2" to use my pseudo-XML of makefaq 2.x.
      # You could use "-r 3", but that XML format is not yet implemented.
      #
      self.fileformat = 2

      #
      # set the default delimiter in a single-line file
      #
      self.delimiter = '|'

      #
      # set the default delimiters used in multi-line files
      #
      self.cdelim = "<c>"
      self.qdelim = "<q>"
      self.adelim = "<a>"

      #
      # internationalization and localization
      # Tries to use the LANG env variable first. Failing that, it
      # falls back on the LOCALE defined at the top of the file.
      #
      try:
          self.locale=os.environ['LANG']
      except:
          self.locale = LOCALE

      LocalizeStrings(self, self.locale)

      #
      # timestamp
      #
      self.TS = {
         'Pre'   : '<p><i>',
         'Post'  : '</i></p>',
         'Pre+'  : '',
         'Post+' : ''
         }

      # headings
      self.Head = {
         'Pre'   : '<hr><h2>',
         'Post'  : '</h2>',
         'Pre+'  : '',
         'Post+' : ''
         }

      # sections
      self.Sec = {
         'Pre'   : '<dl>',
         'Post'  : '</dl>',
         'Pre+'  : '',
         'Post+' : ''
         }

      # table of contents
      self.TOC = {
         'Pre'       : '<dl>',
         'Post'      : '</dl>',
         'Pre+'      : '',
         'Post+'     : '',
         'CatPre'    : '<dt><b>',
         'CatPost'   : '</b></dt>',
         'ListPre'   : '<dd><ul>',
         'ListPost'  : '</ul></dd>',
         'EntryPre'  : '<li><a href="#',
         'EntryIn'   : '">',
         'EntryPost' : '</a></li>'
         }

      # questions
      self.Q = {
         'Pre'  : '<dt><b><a name="',
         'In'   : '\">',
         'Post' : '</a></b></dt>'
         }

      # answers
      self.A = {
         'Pre'  : '<dd>',
         'Post' : '<br><br></dd>'
         }

      # This flag is for adding a link to return to the top of
      # the page after every answer
      self.addJumps = FALSE

# -------------------------------------------------------------

class TextConfig(DefaultConfig):
   """ Text output configuration """
   def __init__(self):
      DefaultConfig.__init__(self)

      # ID
      self.name = 'text'

      # flags
      self.hasLinks = FALSE

      # filenames
      self.headfile = 'faqheader.txt'
      self.footfile = 'faqfooter.txt'
      self.infile   = 'faq.dat'
      self.outfile  = 'faq.txt'

      # default delimiter
      self.delimiter = '|'

      # timestamp
      self.TS['Pre']   = '\n'
      self.TS['Post']  = '\n\n'
      self.TS['Pre+']  = ''
      self.TS['Post+'] = ''

      # heading
      self.Head['Pre']  = ''
      self.Head['Post'] = '\n'
      self.Head['Pre+']  = ''
      self.Head['Post+'] = ''

      # sections
      self.Sec['Pre']  = ''
      self.Sec['Post'] = ''
      self.Sec['Pre+']  = ''
      self.Sec['Post+'] = ''

      # TOC
      self.TOC['Pre']       = ''
      self.TOC['Post']      = '\n'
      self.TOC['Pre+']      = ''
      self.TOC['Post+']     = ''
      self.TOC['CatPre']    = ''
      self.TOC['CatPost']   = ''
      self.TOC['ListPre']   = ''
      self.TOC['ListPost']  = '\n'
      self.TOC['EntryPre']  = ''
      self.TOC['EntryIn']   = ''
      self.TOC['EntryPost'] = ''

      # questions
      self.Q['Pre']  = ''
      self.Q['In']   = ''
      self.Q['Post'] = '\n'

      # answers
      self.A['Pre']  = ''
      self.A['Post'] = '\n'


# -------------------------------------------------------------

class ScreenConfig(DefaultConfig):
   """ screen (text) output configuration """

   def __init__(self):
      DefaultConfig.__init__(self)

      # ID
      self.name = 'screen'

      # flags
      self.hasLinks = FALSE

      # filenames
      self.headfile = 'faqheader.txt'
      self.footfile = 'faqfooter.txt'
      self.infile   = 'faq.dat'
      self.outfile  = 'STDOUT'

      # default delimiter
      self.delimiter = '|'

      # timestamp
      self.TS['Pre']   = '\n'
      self.TS['Post']  = '\n\n'
      self.TS['Pre+']  = ''
      self.TS['Post+'] = ''

      # heading
      self.Head['Pre']  = ''
      self.Head['Post'] = '\n'
      self.Head['Pre+']  = ''
      self.Head['Post+'] = ''

      # sections
      self.Sec['Pre']  = ''
      self.Sec['Post'] = ''
      self.Sec['Pre+']  = ''
      self.Sec['Post+'] = ''

      # TOC
      self.TOC['Pre']       = ''
      self.TOC['Post']      = '\n'
      self.TOC['Pre+']      = ''
      self.TOC['Post+']     = ''
      self.TOC['CatPre']    = ''
      self.TOC['CatPost']   = ''
      self.TOC['ListPre']   = ''
      self.TOC['ListPost']  = '\n'
      self.TOC['EntryPre']  = ''
      self.TOC['EntryIn']   = ''
      self.TOC['EntryPost'] = ''

      # questions
      self.Q['Pre']  = ''
      self.Q['In']   = ''
      self.Q['Post'] = '\n'

      # answers
      self.A['Pre']  = ''
      self.A['Post'] = '\n'


# -------------------------------------------------------------

class DocBookXMLConfig(DefaultConfig):
   """Configuration to create DocBook XML
   
   Target is to have entries like:

   <qandaentry>
   <question id="4">
   <para>Will the product still be called xxxxxx</para>
   </question>
   <answer>
   <para>That has not been determined yet.</para>
   </answer>
   </qandaentry>
   """

   def __init__(self):
      DefaultConfig.__init__(self)

      self.name = "DocBookXML"

      # Don't create a TOC, use numbering or create links
      self.createTOC = FALSE
      self.numberQuestions = FALSE
      self.hasLinks = FALSE

      self.headfile = 'faqheader.xml'
      self.footfile = 'faqfooter.xml'
      self.infile   = 'faq.dat'
      self.outfile  = 'faq-output.xml'

      # timestamp
      #
      # NEED TO WORK THIS ONE OUT
      #

      self.TS = {
         'Pre'   : '<para><emphasis>',
         'Post'  : '</emphasis></para>',
         'Pre+'  : '',
         'Post+' : ''
         }

      # headings
      #
      # This may seem strange to put the <qandadiv> in the Pre+
      # part of the headings, but this is necessary because HTML
      # headings are outside of a structure, while XML headings
      # are inside of an structure.
      #
      self.Head = {
         'Pre'   : '<title>',
         'Post'  : '</title>',
         'Pre+'  : '<qandadiv>\n',
         'Post+' : ''
         }

      # sections
      self.Sec = {
         'Pre'   : '',
         'Post'  : '</qandadiv>\n',
         'Pre+'  : '',
         'Post+' : ''
         }

      # questions
      self.Q = {
         'Pre'  : '<qandaentry>\n<question>\n<para>',
         'In'   : '',
         'Post' : '</para>\n</question>'
         }
      #
      # possible definition to get id into <question>
      # currently not used.
      #self.Q = {
      #   'Pre'  : '<qandaentry>\n<question id="',
      #   'In'   : '">\n<para>',
      #   'Post' : '</para>\n</question>'
      #   }

      # answers
      self.A = {
         'Pre'  : '<answer>\n<para>',
         'Post' : '</para>\n</answer>\n</qandaentry>\n'
         }

# -------------------------------------------------------------
class BEASTConfig(DefaultConfig):
   """BEAST configuration
   Sample configuration provided by Dave Seidel
   (dave@superluminal.com)"""

   def __init__(self):
      DefaultConfig.__init__(self)

      # ID
      self.name = 'BEAST'
      
      # filenames
      self.headfile = 'html.1.faq'
      self.footfile = 'html.2.faq'
      self.infile   = 'faq.dat'
      self.outfile  = 'faq.html'

      # timestamp
      self.TS['Pre+']  = '<tr><td>'
      self.TS['Post+'] = '</td></tr>'

      # headings
      self.Head['Pre']   = ''
      self.Head['Post']  = ''
      self.Head['Pre+']  = '<tr><td bgcolor="#005D5D"><font face="Lucida, Verdana, Arial, sans-serif" color="#D0E4D0" size="+2">'
      self.Head['Post+'] = '</font></td></tr>'

      # sections
      self.Sec['Pre+']  = '<tr><td><font face="Lucida, Verdana, Arial, sans-serif">'
      self.Sec['Post+'] = '</font></td></tr>'

      # table of contents
      self.TOC['Pre+']  = '<tr><td><font face="Lucida, Verdana, Arial, sans-serif">'
      self.TOC['Post+'] = '</font></td></tr>'


# -------------------------------------------------------------
#
# table of available configurations; if you add a new
# configuration, please add its class name to this list
#
# -------------------------------------------------------------

configTab = [
   DefaultConfig,
   TextConfig,
   ScreenConfig,
   DocBookXMLConfig,
   BEASTConfig
   ]

# -------------------------------------------------------------

def PrintConfigs():
   """Tells each member of configTab to print itself"""

   print 'Available configurations:'
   for i in configTab:
      cfg = i()
      cfg.show()

# -------------------------------------------------------------

def FindConfig(name):
   """Given a config name, attempts to find a matching entry
      in configTab; if found returns an *instance* of the
      matching class"""

   for i in configTab:
      cfg = i()
      if name == str(cfg):
         return cfg

# -------------------------------------------------------------

class FaqEntry:
   """ Class defining an individual FAQ entry """

   def __init__(self,content):
      self.question = content[0]
      self.answer = content[1]
      
   def __repr__(self):
      return "\n" +  self.question +  "\n" +  self.answer

# -------------------------------------------------------------

def IncludeFile(out, inputfile):
   """Reads in a file and writes it out, with an error message."""
   try:
      input = open(inputfile, 'r')
   except:
      stderr.write('Error opening file ' + inputfile + ' for inclusion.\n')
      exit(1)
   text = input.read()
   out.write(text)

# -------------------------------------------------------------

def FixSpecialText(text):
   """This is where we strip and/or transform certain HTML tags
      for plain-text output formats"""

   # <br> becomes \n
   fixed = sub('<br>', '\n', text)

   # <a></a> gets stripped (use '?' qualifier for a non-greedy match)
   fixed = sub('<a href=".+?">', '', fixed)
   fixed = sub('</a>', '', fixed)

   #<i>foo</i> becomes *foo*
   fixed = sub('<i>', '*', fixed)
   fixed = sub('</i>', '*', fixed)
   fixed = sub('<em>', '*', fixed)
   fixed = sub('</em>', '*', fixed)

   # </li> becomes "; " (so at least we get a semicolon-separated list)
   fixed = sub('</li>', '; ', fixed)

   # Need to figure out how to strip out &lt; and &gt; and replace them
   # with < and >
   #fixed = sub('&lt;', '<', fixed)
   #fixed = sub('&gt;', '>', fixed)

   # strip everything else
   fixed = sub('<.+?>', '', fixed)

   return fixed

# -------------------------------------------------------------

def ReadOrigSource(cfg):
   """The function below is the original ReadSource that reads in faq.dat
   files with all the contents on a single long line.  It has been 
   retained here to provide backward compatibility so that older data
   files can still be used.  At some future point, it will be merged
   back in with the new ReadSource to have a single function."""

   try:
      input = open(cfg.infile, 'r')
   except:
      stderr.write('Error opening file ' + cfg.infile + ' as input.\n')
      exit(1)

   faq1 = {}
   catlist = []

   i = 1
   for line in input.readlines():
      x = split(line, cfg.delimiter)
      if len(x) < 3:
         print 'Error: ' + cfg.infile + ', line ' + str(i) + ': bad format'
         return
      i = i + 1
      category = strip(x[0])
      x[1] = strip(x[1])
      x[2] = strip(x[2])

      # clean up answer question/text
      if not cfg.hasLinks:
         x[1] = FixSpecialText(x[1])
         x[2] = FixSpecialText(x[2])

      # if the category exists, append the entry
      # otherwise add a new category, *then* append the entry.
      if faq1.has_key(category):
         faq1[category].append(FaqEntry(x[1:]))
      else:
         catlist.append(category)
         faq1[category] = []
         faq1[category].append(FaqEntry(x[1:]))
   input.close()
   return faq1, catlist

# -------------------------------------------------------------

def ReadPseudoXMLSource(cfg):
   """The ReadPseudoSource below handles multiline input in a pseudo-XML 
      format."""

   try:
      input = open(cfg.infile, 'r')
   except:
      stderr.write('Error opening file ' + cfg.infile + ' as input.\n')
      exit(1)

   faq1 = {}
   catlist = []

   i = 1
     # read in entire file
   all = input.read()    
     # split into blocks on category delimiter (default is <c>)
   blocks = split(all,cfg.cdelim)

   for line in blocks[1:]:
      try:
         a = split(line, cfg.qdelim)
	 b = split(a[1], cfg.adelim)
	 x = [a[0], b[0], b[1]]
      except:
         print 'Error: ' + cfg.infile + ', question ' + str(i) + ': bad format'
         return

      if len(x) < 3:
         print 'Error: ' + cfg.infile + ', question ' + str(i) + ': bad format'
         return
      i = i + 1
      category = strip(x[0])
      x[1] = strip(x[1])
      x[2] = strip(x[2])

      # (v2.1)The following line was suggested by Nicolas Devillard and 
      # basically makes any "paragraph" in the data file into an HTML 
      # paragraph, i.e. you have lines of text, a blank line, and then 
      # more text. It's really just a hack to avoid typing extra <p>'s 
      # in the .dat file.  He asked for it and I am including it here 
      # COMMENTED OUT for those who wish to enable this setting. I do not
      # enable it by default because it may generate extra <p>'s in other
      # HTML code where people do not want them to be.
      #
      #x[2] = sub('\n\n','\n<p>\n',x[2])


      # clean up answer question/text
      if not cfg.hasLinks:
         x[1] = FixSpecialText(x[1])
         x[2] = FixSpecialText(x[2])

      # if the category exists, append the entry
      # otherwise add a new category, *then* append the entry.
      if faq1.has_key(category):
         faq1[category].append(FaqEntry(x[1:]))
      else:
         catlist.append(category)
         faq1[category] = []
         faq1[category].append(FaqEntry(x[1:]))
   input.close()
   return faq1, catlist

# -------------------------------------------------------------

def PrintTimeStamp(cfg, out):
   """ This function prints out the timestamp for when the FAQ was 
   revised.  It first attempts to set the locale so that the timestamp
   will be generated using the date/time format of your location.
   NOTE that on non-Linux platforms, there seems to be a problem setting
   the locale, so it may just use whatever system-generated date/time is
   supplied by the operating system."""

   try:
       # First try to set to locale to whatever the user (or system) has
       # configured
       locale.setlocale(locale.LC_ALL,cfg.locale)
   except locale.Error:
       # If that fails, default to 'en_US'
       try:
           locale.setlocale(locale.LC_ALL,"en_US")
           stderr.write("Locale %s not supported. Using 'en_US' instead." % cfg.locale)
       except:
           #If there is a problem with setting the locale, do nothing and just
	   # use whatever date/time the system provides
           pass

   out.write("%s%s%s %s%s%s\n" % (cfg.TS['Pre+'], cfg.TS['Pre'],cfg.RevString,
                          strftime("%A %d %B %Y %H:%M:%S",localtime(time())),
                                              cfg.TS['Post'], cfg.TS['Post+']))


# -------------------------------------------------------------

def PrintTOC(cfg, out, faq1, catlist):
   """Prints out the "table of contents" - the initial list of questions 
      with their links to the questions further below on the page."""

   out.write("%s%s%s%s%s\n" % (cfg.Head['Pre+'], cfg.Head['Pre'], cfg.TOCString,\
                                              cfg.Head['Post'], cfg.Head['Post+']))

   out.write("%s%s\n" % (cfg.Sec['Pre+'], cfg.Sec['Pre']))
   i = 1
   for x in catlist:
      if cfg.numberQuestions:
         out.write("%s%s. %s%s\n" % (cfg.TOC['CatPre'],
                                  str(i), x,
                                  cfg.TOC['CatPost']))
      else:
         out.write("%s%s%s\n" % (cfg.TOC['CatPre'],
                                  x,
                                  cfg.TOC['CatPost']))
      out.write("%s\n" % cfg.TOC['ListPre'])
      if cfg.hasLinks and cfg.numberQuestions:
         for y in range(len(faq1[x])):
            out.write("%s%s%s%s%s.%s. %s%s\n" % (cfg.TOC['EntryPre'],
                                                 x, str(y),
                                                 cfg.TOC['EntryIn'],
                                                 str(i), str(y + 1),
                                                 faq1[x][y].question,
                                                 cfg.TOC['EntryPost']))
      elif cfg.hasLinks:
         for y in range(len(faq1[x])):
            out.write("%s%s%s%s%s%s\n" % (cfg.TOC['EntryPre'],
                                                 x, str(y),
                                                 cfg.TOC['EntryIn'],
                                                 faq1[x][y].question,
                                                 cfg.TOC['EntryPost']))
      elif cfg.numberQuestions:
         for y in range(len(faq1[x])):
            out.write("%s%s%s.%s. %s%s\n" % (cfg.TOC['EntryPre'],
                                             cfg.TOC['EntryIn'],
                                             str(i), str(y + 1),
                                             faq1[x][y].question,
                                             cfg.TOC['EntryPost']))
      else:
         for y in range(len(faq1[x])):
            out.write("%s%s%s%s\n" % (cfg.TOC['EntryPre'],
                                             cfg.TOC['EntryIn'],
                                             faq1[x][y].question,
                                             cfg.TOC['EntryPost']))
            
      out.write("%s\n" % cfg.TOC['ListPost'])
      i = i + 1
   out.write("%s%s\n" % (cfg.Sec['Post'], cfg.Sec['Post+']))

# -------------------------------------------------------------

def PrintQA(cfg, out, faq1, feedback, catlist):
   """Prints out the Questions and corresponding Answers"""

   i = 1
   for x in catlist:
      if cfg.numberQuestions:
         out.write("%s%s%s. %s%s%s\n" % (cfg.Head['Pre+'], cfg.Head['Pre'],
                                      str(i), x,
                                      cfg.Head['Post'], cfg.Head['Post+']))
      else:
         out.write("%s%s%s%s%s\n" % (cfg.Head['Pre+'], cfg.Head['Pre'],
                                      x,
                                      cfg.Head['Post'], cfg.Head['Post+']))

      out.write("%s%s\n" % (cfg.Sec['Pre+'],
                            cfg.Sec['Pre']))

      for y in range(len(faq1[x])):
         if cfg.hasLinks and cfg.numberQuestions:          
            out.write("%s%s%s%s%s.%s. %s%s\n" % (cfg.Q['Pre'],
                                                 x, str(y),
                                                 cfg.Q['In'],
                                                 str(i), str(y + 1),
                                                 faq1[x][y].question,
                                                 cfg.Q['Post']))
         elif cfg.hasLinks:          
            out.write("%s%s%s%s%s%s\n" % (cfg.Q['Pre'],
                                                 x, str(y),
                                                 cfg.Q['In'],
                                                 faq1[x][y].question,
                                                 cfg.Q['Post']))
         elif cfg.numberQuestions:          
            out.write("%s%s%s.%s. %s%s\n" % (cfg.Q['Pre'],
                                             cfg.Q['In'],
                                             str(i), str(y + 1),
                                             faq1[x][y].question,
                                             cfg.Q['Post']))
         else:
            out.write("%s%s%s%s\n" % (cfg.Q['Pre'],
                                             cfg.Q['In'],
                                             faq1[x][y].question,
                                             cfg.Q['Post']))
         out.write("%s%s%s\n" % (cfg.A['Pre'],
                                 faq1[x][y].answer,
                                 cfg.A['Post']))
         if cfg.addJumps:
	     out.write('<dd><p><a href="#top">%s</a></p></dd>' % cfg.JumpString)

         if feedback == TRUE:
             stdout.write('.')
      out.write("%s%s\n" % (cfg.Sec['Post'], cfg.Sec['Post+']))
      i = i + 1


# -------------------------------------------------------------

def BuildFAQ(cfg, feedback, catsort):
   """This function builds the actual FAQ output file, including 
      reading in the data from the data file."""

   #
   # check to see if we're sending to STDOUT and if we are, squelch the
   # verbose feedback
   #
   if cfg.outfile == "STDOUT":
      out = stdout
      feedback = FALSE
   #
   # otherwise try writing the file for output
   #
   else:
      try:
         out = open(cfg.outfile, 'w')
      except:
         stderr.write('Error opening file ' + cfg.outfile + ' for output, exiting.\n')
         exit(1)

   # 
   # if '-r' was used on the command line, or if the flag was set in the config,
   # use the old, single-line data file format. Otherwise, use multi-line format.
   #
   if cfg.fileformat == 1:
      faq,catlist = ReadOrigSource(cfg)

   else:
      faq,catlist = ReadPseudoXMLSource(cfg)

   #
   # if the faq came back undefined, exit out of here
   #
   if not faq:
      return

   #
   # if '-s' was used, sort the categories alphabetically
   #
   if catsort == TRUE:
      catlist.sort()

   #
   # Set up header info - the header text, timestamp and list of questions 
   # (which is the TOC)
   #
   IncludeFile(out, cfg.headfile)
   PrintTimeStamp(cfg, out)

   if cfg.createTOC == TRUE:
      PrintTOC(cfg, out, faq, catlist)

   #
   # if verbose output is turned on (-v), give some feedback.
   #
   if feedback == TRUE:
      print "\nWriting FAQ info to "+ cfg.outfile,

   #
   # print out questions and answers
   #
   PrintQA(cfg, out, faq, feedback, catlist)

   #
   # print out footer file
   #
   IncludeFile(out, cfg.footfile)

   # provide final verbose feedback
   #
   if feedback == TRUE:
      print "done.\n"

# -------------------------------------------------------------

def PrintHelp():
   """Prints out help"""
	 
   print 'Usage: makefaq [-h] [-v] [-n] [-N] [-l] [-s] [-j] [-c config-name]' + \
         ' [-i input-file] [-o output-file] [-t header-file] [-b footer-file]' + \
	 ' [-d delimiter] [-r fileformatrevision]\n' + \
         '\n' + \
         'Hints:\n' + \
         '  - If you say "-v" (verbose), the default config settings will be displayed.\n' + \
         '  - Use -l to list all the configurations.\n' + \
         '  - Use -i, -o, -t, and -b to override config settings.\n' + \
         '  - You can say: "-o STDOUT".\n' + \
         '  - Use "-n" to test your config settings without doing anything.\n' + \
         '  - Use "-N" to suppress all line numbers.\n' + \
         '  - Use "-r" to revert to using the older data formats.\n' + \
         '            *  Use "-r 1" to use the original single-line format\n' + \
         '  - Use "-d" to use a specific character as the delimiter.\n' + \
         '             ("-d" only works with "-r" and the old file format)\n' + \
         '  - Use "-L" to use a specific locale (see README).\n' + \
         '  - Use "-j" to add "Return to top of page" links after every entry.\n' + \
         '  - Use "-s" to sort the categories in alphabetical order.\n'

# -------------------------------------------------------------

def main():
   """main routine"""
   #
   # set various flags
   #
   do_nothing = FALSE
   verbose = FALSE
   feedback = TRUE
   catsort = FALSE

   # storage for user choices on command line
   user = {
      'cfg' : None,  # configuration instance
      'i'   : None,  # input filename
      'o'   : None,  # output filename
      't'   : None,  # header filename
      'b'   : None,  # footer filename
      'd'   : None,  # delimiter
      'L'   : None,  # locale
      'j'   : FALSE, # return to top of page links are NOT included
      'N'   : TRUE,  # use numbering by default
      'r'   : 2      # default to format "2" or pseudo-XML 
      }

   # process the command line
   try:
      opts, args = getopt.getopt(argv[1:], "hvnlsjNc:r:i:o:t:b:d:L:")
   except getopt.error, msg:
      print 'Error: ' + msg
      exit(2)
   for i in opts:
      if i[0] == '-h':
         PrintHelp()
         exit(0)
      elif i[0] =='-l':
         PrintConfigs()
         exit(0)
      elif i[0] == '-v':
         verbose = TRUE
      elif i[0] == '-n':
         do_nothing = TRUE
      elif i[0] == '-s':
         catsort = TRUE
      elif i[0] == '-c':
         user['cfg'] = FindConfig(i[1])
         if user['cfg'] == None:
            print 'Sorry, there is no configuration called ' + i[1]
            exit(2)
      elif i[0] == '-i':
         user['i'] = i[1]
      elif i[0] == '-o':
         user['o'] = i[1]
      elif i[0] == '-t':
         user['t'] = i[1]
      elif i[0] == '-b':
         user['b'] = i[1]
      elif i[0] == '-d':
         user['d'] = i[1]
      elif i[0] == '-L':
         user['L'] = i[1]
      elif i[0] == '-j':
         user['j'] = TRUE
      elif i[0] == '-N':
         user['N'] = FALSE
      elif i[0] == '-r':
         user['r'] = atoi(i[1])

   # commit the user choices; we do it this way to ensure that cfg
   # gets set before we try to set its attributes
   if user['cfg']:
      cfg = user['cfg']
   else:
      cfg = DefaultConfig()

   if user['i']:
      cfg.infile = user['i']
   if user['o']:
      cfg.outfile = user['o']
   if user['t']:
      cfg.headfile = user['t']
   if user['b']:
      cfg.footfile = user['b']
   if user['d']:
      cfg.delimiter = user['d']
   if user['L']:
      cfg.locale = user['L']
      LocalizeStrings(cfg, cfg.locale)

   cfg.fileformat = user['r']
   cfg.addJumps = user['j']
   cfg.numberQuestions = user['N']

   if verbose:
      cfg.show()
   if do_nothing:
      print 'Skipping file processing.'
   else:
      BuildFAQ(cfg, feedback, catsort)


# Start main loop

if __name__ == '__main__':

   main()
