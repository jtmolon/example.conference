from five import grok

from z3c.form import group, field
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Item

from plone.directives import dexterity, form
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable


from example.conference import MessageFactory as _
from plone.app.textfield import RichText
from plone.supermodel import model
from zope import schema


# Interface class; used to define content-type schema.

class ISession(model.Schema):
    """
    A Session in a conference
    """
    title = schema.TextLine(
            title=_(u"Title"),
            description=_(u"Session title"),
        )

    description = schema.Text(
            title=_(u"Session summary"),
        )

    details = RichText(
            title=_(u"Session details"),
            required=False
        )


# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class Session(Item):
    grok.implements(ISession)

    # Add your class methods and properties here
    pass


# View class
# The view will automatically use a similarly named template in
# session_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class SampleView(grok.View):
    """ sample view class """

    grok.context(ISession)
    grok.require('zope2.View')

    # grok.name('view')

    # Add view methods here
