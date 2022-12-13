from datetime import timedelta

import pytest
from pydantic import ValidationError

from meowgic_matt.models import (
    Channel,
    Enclosure,
    Guid,
    Item,
    ITunesCategories,
    ITunesCategory,
    ITunesSubcategories,
    ITunesSubcategory,
    Owner,
)


def test_category_validates_subcategories_correctly():
    cat = ITunesCategory(name=ITunesCategories.ARTS)

    arts_subcategory = ITunesSubcategory(name=ITunesSubcategories.BOOKS)
    cat = ITunesCategory(name=ITunesCategories.ARTS, subcategories=[arts_subcategory])

    second_arts_subcategory = ITunesSubcategory(name=ITunesSubcategories.FOOD)
    cat = ITunesCategory(
        name=ITunesCategories.ARTS,
        subcategories=[arts_subcategory, second_arts_subcategory],
    )

    science_subcategory = ITunesSubcategory(name=ITunesSubcategories.ASTRONOMY)
    with pytest.raises(ValidationError):
        # Should not allow a mismatched category
        cat = ITunesCategory(
            name=ITunesCategories.ARTS, subcategories=[science_subcategory]
        )

    with pytest.raises(ValidationError):
        # Should not allow a mismatched category even if another one matches
        cat = ITunesCategory(
            name=ITunesCategories.ARTS,
            subcategories=[arts_subcategory, science_subcategory],
        )

    with pytest.raises(ValidationError):
        # Should not allow any category
        cat = ITunesCategory(
            name=ITunesCategories.GOVERNMENT,
            subcategories=[arts_subcategory, science_subcategory],
        )


def test_export_enclosure_as_xml():
    enclosure = Enclosure(url="http://meow.com", length=3)

    assert (
        enclosure.to_xml()
        == "<enclosure url='http://meow.com' length='3' type='audio/mpeg'/>"
    )


def test_export_guid_as_xml():
    guid = Guid(id="meow", is_permalink=True)

    assert guid.to_xml() == "<guid isPermaLink='true'>meow</guid>"


def test_full_channel_thing():
    owner = Owner(itunes_name="Meow my itunes name", itunes_email="and also my email")

    cat = ITunesCategory(name=ITunesCategories.ARTS)
    subcat = ITunesSubcategory(name=ITunesSubcategories.CAREERS)
    cat2 = ITunesCategory(name=ITunesCategories.BUSINESS, subcategories=[subcat])

    enclosure = Enclosure(
        url="http://enclosure.url",
        length="12345",
    )
    guid = Guid(
        id="guid123",
        is_permalink=False,
    )

    item1 = Item(
        title="My cool item",
        itunes_author="item author",
        itunes_subtitle="the subtitle of my item",
        description="and the description of the item",
        itunes_summary="but also the summary",
        enclosure=enclosure,
        guid=guid,
        pub_date="2022-02-01",  # figure out how to convert to string in the right format
        itunes_duration=timedelta(minutes=24, seconds=10, hours=1),
    )

    channel = Channel(
        title="My Cool Podcast",
        link="http://meow.com",
        language="meow",
        copyright="copyright stuff",
        itunes_subtitle="my cool subtitle",
        itunes_author="I am an author",
        description="This is a description",
        itunes_summary="this, by contrast, is a summary",
        itunes_owner=owner,
        itunes_image="http://image.xyz",
        itunes_categories=[cat, cat2],
        itunes_explicit=True,
        items=[item1],
    )

    assert (
        channel.to_xml()
        == """
        <?xml version='1.0' encoding='UTF-8'?>
        <rss xmlns:itunes='http://www.itunes.com/dtds/podcast-1.0.dtd' version='2.0'>
        <channel>
        <title>My Cool Podcast</title>
        <link>http://meow.com</link>
        <language>meow</language>
        <copyright>copyright stuff</copyright>
        <itunes:subtitle>my cool subtitle</itunes:subtitle>
        <itunes:author>I am an author</itunes:author>
        <itunes:summary>this, by contrast, is a summary</itunes:summary>
        <description>This is a description</description>
        <itunes:owner>
        <itunes:name>Meow my itunes name</itunes:name>
        <itunes:email>and also my email</itunes:email>
        </itunes:owner>
        <itunes:image>http://image.xyz</itunes:image>
        <itunes:category text='Arts'/>
<itunes:category text='Business'>
            <itunes:category text='Careers'/>
            </itunes:category>

        <itunes:explicit>true</itunes:explicit>
        <item>
        <title>My cool item</title>
        <itunes:author>item author</itunes:author>
        <itunes:subtitle>the subtitle of my item</itunes:subtitle>
        <itunes:summary><![CDATA[but also the summary]]></itunes:summary>
        <description><![CDATA[and the description of the item]]></description>
        <enclosure url='http://enclosure.url' length='12345' type='audio/mpeg'/>
        <guid isPermaLink='false'>guid123</guid>
        <pubDate>Tue, 01 Feb 2022 00:00:00 EST</pubDate>
        <itunes:duration>1:24:10</itunes:duration>
        </item>
        </channel>
        </rss>
        """
    )
