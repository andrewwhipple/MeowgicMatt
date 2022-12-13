from datetime import date, timedelta
from enum import Enum
from typing import Optional

from pydantic import BaseModel, HttpUrl, validator


class ITunesSubcategories(Enum):
    # Arts
    BOOKS = "Books"
    DESIGN = "Design"
    FASHION_AND_BEAUTY = "Fashion &amp; Beauty"
    FOOD = "Food"
    PERFORMING_ARTS = "Performing Arts"
    VISUAL_ARTS = "Visual Arts"

    # Business
    CAREERS = "Careers"
    ENTREPRENEURSHIP = "Entrepreneurship"
    INVESTING = "Investing"
    MANAGEMENT = "Management"
    MARKETING = "Marketing"
    NON_PROFIT = "Non-Profit"

    # Comedy
    COMEDY_INTERVIEWS = "Comedy Interviews"
    IMPROV = "Improv"
    STAND_UP = "Stand-Up"

    # Education
    COURSES = "Courses"
    HOW_TO = "How To"
    LANGUAGE_LEARNING = "Language Learning"
    SELF_IMPROVEMENT = "Self-Improvement"

    # Fiction
    COMEDY_FICTION = "Comedy Fiction"
    DRAMA = "Drama"
    SCIENCE_FICTION = "Science Fiction"

    # Health & Fitness
    ALTERNATIVE_HEALTH = "Alternative Health"
    FITNESS = "Fitness"
    MEDICINE = "Medicine"
    MENTAL_HEALTH = "Mental Health"
    NUTRITION = "Nutrition"
    SEXUALITY = "Sexuality"

    # Kids & Family
    EDUCATION_FOR_KIDS = "Education for Kids"
    PARENTING = "Parenting"
    PETS_AND_ANIMALS = "Pets &amp; Animals"
    STORIES_FOR_KIDS = "Stories for Kids"

    # Leisure
    ANIMATION_AND_MANGA = "Animation &amp; Manga"
    AUTOMOTIVE = "Automotive"
    AVIATION = "Aviation"
    CRAFTS = "Crafts"
    GAMES = "Games"
    HOBBIES = "Hobbies"
    HOME_AND_GARDEN = "Home &amp; Garden"
    VIDEO_GAMES = "Video Games"

    # Music
    MUSIC_COMMENTARY = "Music Commentary"
    MUSIC_HISTORY = "Music History"
    MUSIC_INTERVIEWS = "Music Interviews"

    # News
    BUSINESS_NEWS = "Business News"
    DAILY_NEWS = "Daily News"
    ENTERTAINMENT_NEWS = "Entertainment News"
    NEWS_COMMENTARY = "News Commentary"
    POLITICS = "Politics"
    SPORTS_NEWS = "Sports News"
    TECH_NEWS = "Tech News"

    # Religion & Spirituality
    BUDDHISM = "Buddhism"
    CHRISTIANITY = "Christianity"
    HINDUISM = "Hinduism"
    ISLAM = "Islam"
    JUDAISM = "Judaism"
    RELIGION = "Religion"
    SPIRITUALITY = "Spirituality"

    # Science
    ASTRONOMY = "Astronomy"
    CHEMISTRY = "Chemistry"
    EARTH_SCIENCES = "Earth Sciences"
    LIFE_SCIENCES = "Life Sciences"
    MATHEMATICS = "Mathematics"
    NATURAL_SCIENCES = "Natural Sciences"
    NATURE = "Nature"
    PHYSICS = "Physics"
    SOCIAL_SCIENCES = "Social Sciences"

    # Society & Culture
    DOCUMENTARY = "Documentary"
    PERSONAL_JOURNALS = "Personal Journals"
    PHILOSOPHY = "Philosophy"
    PLACES_AND_TRAVEL = "Places &amp; Travel"
    RELATIONSHIPS = "Relationships"

    # Sports
    BASEBALL = "Baseball"
    BASKETBALL = "Basketball"
    CRICKET = "Cricket"
    FANTASY_SPORTS = "Fantasy Sports"
    FOOTBALL = "Football"
    GOLF = "Golf"
    HOCKEY = "Hockey"
    RUGBY = "Rugby"
    SOCCER = "Soccer"
    SWIMMING = "Swimming"
    TENNIS = "Tennis"
    VOLLEYBALL = "Volleyball"
    WILDERNESS = "Wilderness"
    WRESTLING = "Wrestling"

    # TV & Film
    AFTER_SHOWS = "After Shows"
    FILM_HISTORY = "Film History"
    FILM_INTERVIEWS = "Film Interviews"
    FILM_REVIEWS = "Film Reviews"
    TV_REVIEWS = "TV Reviews"


class ITunesCategories(Enum):
    ARTS = "Arts"
    BUSINESS = "Business"
    COMEDY = "Comedy"
    EDUCATION = "Education"
    FICTION = "Fiction"
    GOVERNMENT = "Government"
    HISTORY = "History"
    HEALTH_AND_FITNESS = "Health &amp; Fitness"
    KIDS_AND_FAMILY = "Kids &amp; Family"
    LEISURE = "Leisure"
    MUSIC = "Music"
    NEWS = "News"
    RELIGION_AND_SPIRITUALITY = "Religion &amp; Spirituality"
    SCIENCE = "Science"
    SOCIETY_AND_CULTURE = "Society &amp; Culture"
    SPORTS = "Sports"
    TECHNOLOGY = "Technology"
    TRUE_CRIME = "True Crime"
    TV_AND_FILM = "TV &amp; Film"


CATEGORY_SUBCATEGORY_TREE = {
    ITunesCategories.ARTS: [
        ITunesSubcategories.BOOKS,
        ITunesSubcategories.DESIGN,
        ITunesSubcategories.FASHION_AND_BEAUTY,
        ITunesSubcategories.FOOD,
        ITunesSubcategories.PERFORMING_ARTS,
        ITunesSubcategories.VISUAL_ARTS,
    ],
    ITunesCategories.BUSINESS: [
        ITunesSubcategories.CAREERS,
        ITunesSubcategories.ENTREPRENEURSHIP,
        ITunesSubcategories.INVESTING,
        ITunesSubcategories.MANAGEMENT,
        ITunesSubcategories.MARKETING,
        ITunesSubcategories.NON_PROFIT,
    ],
    ITunesCategories.COMEDY: [
        ITunesSubcategories.COMEDY_INTERVIEWS,
        ITunesSubcategories.IMPROV,
        ITunesSubcategories.STAND_UP,
    ],
    ITunesCategories.EDUCATION: [
        ITunesSubcategories.COURSES,
        ITunesSubcategories.HOW_TO,
        ITunesSubcategories.LANGUAGE_LEARNING,
        ITunesSubcategories.SELF_IMPROVEMENT,
    ],
    ITunesCategories.FICTION: [
        ITunesSubcategories.COMEDY_FICTION,
        ITunesSubcategories.DRAMA,
        ITunesSubcategories.SCIENCE_FICTION,
    ],
    ITunesCategories.HEALTH_AND_FITNESS: [
        ITunesSubcategories.ALTERNATIVE_HEALTH,
        ITunesSubcategories.FITNESS,
        ITunesSubcategories.MEDICINE,
        ITunesSubcategories.MENTAL_HEALTH,
        ITunesSubcategories.NUTRITION,
        ITunesSubcategories.SEXUALITY,
    ],
    ITunesCategories.KIDS_AND_FAMILY: [
        ITunesSubcategories.EDUCATION_FOR_KIDS,
        ITunesSubcategories.PARENTING,
        ITunesSubcategories.PETS_AND_ANIMALS,
        ITunesSubcategories.STORIES_FOR_KIDS,
    ],
    ITunesCategories.LEISURE: [
        ITunesSubcategories.ANIMATION_AND_MANGA,
        ITunesSubcategories.AUTOMOTIVE,
        ITunesSubcategories.AVIATION,
        ITunesSubcategories.CRAFTS,
        ITunesSubcategories.GAMES,
        ITunesSubcategories.HOBBIES,
        ITunesSubcategories.HOME_AND_GARDEN,
        ITunesSubcategories.VIDEO_GAMES,
    ],
    ITunesCategories.MUSIC: [
        ITunesSubcategories.MUSIC_COMMENTARY,
        ITunesSubcategories.MUSIC_HISTORY,
        ITunesSubcategories.MUSIC_INTERVIEWS,
    ],
    ITunesCategories.NEWS: [
        ITunesSubcategories.BUSINESS_NEWS,
        ITunesSubcategories.DAILY_NEWS,
        ITunesSubcategories.ENTERTAINMENT_NEWS,
        ITunesSubcategories.NEWS_COMMENTARY,
        ITunesSubcategories.POLITICS,
        ITunesSubcategories.SPORTS_NEWS,
        ITunesSubcategories.TECH_NEWS,
    ],
    ITunesCategories.RELIGION_AND_SPIRITUALITY: [
        ITunesSubcategories.BUDDHISM,
        ITunesSubcategories.CHRISTIANITY,
        ITunesSubcategories.HINDUISM,
        ITunesSubcategories.ISLAM,
        ITunesSubcategories.JUDAISM,
        ITunesSubcategories.RELIGION,
        ITunesSubcategories.SPIRITUALITY,
    ],
    ITunesCategories.SCIENCE: [
        ITunesSubcategories.ASTRONOMY,
        ITunesSubcategories.CHEMISTRY,
        ITunesSubcategories.EARTH_SCIENCES,
        ITunesSubcategories.LIFE_SCIENCES,
        ITunesSubcategories.MATHEMATICS,
        ITunesSubcategories.NATURAL_SCIENCES,
        ITunesSubcategories.NATURE,
        ITunesSubcategories.PHYSICS,
        ITunesSubcategories.SOCIAL_SCIENCES,
    ],
    ITunesCategories.SOCIETY_AND_CULTURE: [
        ITunesSubcategories.DOCUMENTARY,
        ITunesSubcategories.PERSONAL_JOURNALS,
        ITunesSubcategories.PHILOSOPHY,
        ITunesSubcategories.PLACES_AND_TRAVEL,
        ITunesSubcategories.RELATIONSHIPS,
    ],
    ITunesCategories.SPORTS: [
        ITunesSubcategories.BASEBALL,
        ITunesSubcategories.BASKETBALL,
        ITunesSubcategories.CRICKET,
        ITunesSubcategories.FANTASY_SPORTS,
        ITunesSubcategories.FOOTBALL,
        ITunesSubcategories.GOLF,
        ITunesSubcategories.HOCKEY,
        ITunesSubcategories.RUGBY,
        ITunesSubcategories.SOCCER,
        ITunesSubcategories.SWIMMING,
        ITunesSubcategories.TENNIS,
        ITunesSubcategories.VOLLEYBALL,
        ITunesSubcategories.WILDERNESS,
        ITunesSubcategories.WRESTLING,
    ],
    ITunesCategories.TV_AND_FILM: [
        ITunesSubcategories.AFTER_SHOWS,
        ITunesSubcategories.FILM_HISTORY,
        ITunesSubcategories.FILM_INTERVIEWS,
        ITunesSubcategories.FILM_REVIEWS,
        ITunesSubcategories.TV_REVIEWS,
    ],
}


class ITunesSubcategory(BaseModel):
    name: ITunesSubcategories


class ITunesCategory(BaseModel):
    name: ITunesCategories
    subcategories: Optional[list[ITunesSubcategory]]

    @validator("subcategories")
    def has_valid_subcategories(cls, v, values):
        if v:
            if values["name"] not in CATEGORY_SUBCATEGORY_TREE:
                raise ValueError(f"{values['name']} has no mapped subcategories")
            for subcategory in v:
                if subcategory.name not in CATEGORY_SUBCATEGORY_TREE[values["name"]]:
                    raise ValueError(
                        f"{subcategory} is not a valid subcategory for {values['name']}"
                    )
        return v

    def to_xml(self):
        if self.subcategories:
            subcategory_list = "\n"
            subcategory_list = subcategory_list.join(
                f"<itunes:category text='{subcategory.name.value}'/>"
                for subcategory in self.subcategories
            )

            return f"""<itunes:category text='{self.name.value}'>
            {subcategory_list}
            </itunes:category>
            """
        else:
            return f"<itunes:category text='{self.name.value}'/>"


class Enclosure(BaseModel):
    url: HttpUrl
    length: int
    type: str = "audio/mpeg"

    def to_xml(self):
        return (
            f"<enclosure url='{self.url}' length='{self.length}' type='{self.type}'/>"
        )


class Guid(BaseModel):
    id: str
    is_permalink: bool

    def to_xml(self):
        return f"<guid isPermaLink='{str(self.is_permalink).lower()}'>{self.id}</guid>"


class Item(BaseModel):
    title: str
    itunes_author: str
    itunes_subtitle: str
    description: str
    itunes_summary: str
    enclosure: Enclosure
    guid: Guid
    pub_date: date
    itunes_duration: timedelta

    def to_xml(self):

        formatted_pub_date = (
            f"{self.pub_date.strftime('%a, %d %b %Y %H:%M:%S')} EST"  # fix timezone
        )

        return f"""<item>
        <title>{self.title}</title>
        <itunes:author>{self.itunes_author}</itunes:author>
        <itunes:subtitle>{self.itunes_subtitle}</itunes:subtitle>
        <itunes:summary><![CDATA[{self.itunes_summary}]]></itunes:summary>
        <description><![CDATA[{self.description}]]></description>
        {self.enclosure.to_xml()}
        {self.guid.to_xml()}
        <pubDate>{formatted_pub_date}</pubDate>
        <itunes:duration>{self.itunes_duration}</itunes:duration>
        </item>"""


class Owner(BaseModel):
    itunes_name: str
    itunes_email: str

    def to_xml(self):
        return f"""<itunes:owner>
        <itunes:name>{self.itunes_name}</itunes:name>
        <itunes:email>{self.itunes_email}</itunes:email>
        </itunes:owner>"""


class Channel(BaseModel):
    title: str
    link: HttpUrl
    language: str = "en-us"
    copyright: str
    itunes_subtitle: str
    itunes_author: str
    description: str
    itunes_summary: str
    itunes_owner: Owner
    itunes_image: HttpUrl
    itunes_categories: list[ITunesCategory]  # Make this an enum
    itunes_explicit: bool
    items: Optional[list[Item]]

    def to_xml(self):
        category_list = "\n"
        category_list = category_list.join(
            f"{category.to_xml()}" for category in self.itunes_categories
        )

        item_list = "\n"
        if self.items:
            item_list = item_list.join(f"{item.to_xml()}" for item in self.items)

        return f"""
        <?xml version='1.0' encoding='UTF-8'?>
        <rss xmlns:itunes='http://www.itunes.com/dtds/podcast-1.0.dtd' version='2.0'>
        <channel>
        <title>{self.title}</title>
        <link>{self.link}</link>
        <language>{self.language}</language>
        <copyright>{self.copyright}</copyright>
        <itunes:subtitle>{self.itunes_subtitle}</itunes:subtitle>
        <itunes:author>{self.itunes_author}</itunes:author>
        <itunes:summary>{self.itunes_summary}</itunes:summary>
        <description>{self.description}</description>
        {self.itunes_owner.to_xml()}
        <itunes:image>{self.itunes_image}</itunes:image>
        {category_list}
        <itunes:explicit>{str(self.itunes_explicit).lower()}</itunes:explicit>
        {item_list}
        </channel>
        </rss>
        """
