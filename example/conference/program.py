from five import grok

from z3c.form import group, field
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Container

from plone.directives import dexterity, form
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable


from example.conference import MessageFactory as _
from plone.app.textfield import RichText
from plone.supermodel import model
from zope import schema


# Interface class; used to define content-type schema.

class IProgram(model.Schema):
    """
    A conference program
    """
    title = schema.TextLine(
            title=_(u"Program name"),
        )

    description = schema.Text(
            title=_(u"Program summary"),
        )

    start = schema.Datetime(
            title=_(u"Start date"),
            required=False,
        )

    end = schema.Datetime(
            title=_(u"End date"),
            required=False,
        )

    details = RichText(
            title=_(u"Details"),
            description=_(u"Details about the program"),
            required=False,
        )    


# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class Program(Container):
    grok.implements(IProgram)

    # Add your class methods and properties here
    pass


# View class
# The view will automatically use a similarly named template in
# program_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class SampleView(grok.View):
    """ sample view class """

    grok.context(IProgram)
    grok.require('zope2.View')

    # grok.name('view')

    # Add view methods here
