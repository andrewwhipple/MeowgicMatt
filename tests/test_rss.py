from meowgic_matt.models import (
    ITunesCategories,
    ITunesCategory,
    ITunesSubcategories,
    ITunesSubcategory,
)
from meowgic_matt.rss import format_category_list


def test_format_category_list_formats_single_categories_correctly():
    category = ITunesCategory(name=ITunesCategories.ARTS)
    category_list = format_category_list(category, None)

    assert category_list == [category]

    subcategory = ITunesSubcategory(name=ITunesSubcategories.NEWS_COMMENTARY)
    category_list = format_category_list(subcategory, None)

    assert category_list == [
        ITunesCategory(name=ITunesCategories.NEWS, subcategories=[subcategory])
    ]


def test_format_category_list_formats_multiple_categories_correctly():
    # Two different categories
    category1 = ITunesCategory(name=ITunesCategories.ARTS)
    category2 = ITunesCategory(name=ITunesCategories.COMEDY)

    category_list = format_category_list(category1, category2)

    assert category_list == [category1, category2]

    # The same category twice
    category_list = format_category_list(category1, category1)
    assert category_list == [category1]

    # Two subcategories from different categories
    subcategory1 = ITunesSubcategory(name=ITunesSubcategories.AFTER_SHOWS)
    subcategory2 = ITunesSubcategory(name=ITunesSubcategories.BUDDHISM)

    main_category_for_subcategory1 = ITunesCategory(
        name=ITunesCategories.TV_AND_FILM, subcategories=[subcategory1]
    )
    main_category_for_subcategory2 = ITunesCategory(
        name=ITunesCategories.RELIGION_AND_SPIRITUALITY, subcategories=[subcategory2]
    )

    category_list = format_category_list(subcategory1, subcategory2)
    assert category_list == [
        main_category_for_subcategory1,
        main_category_for_subcategory2,
    ]

    # Two subcategories from the same category
    subcategory1 = ITunesSubcategory(name=ITunesSubcategories.AFTER_SHOWS)
    subcategory3 = ITunesSubcategory(name=ITunesSubcategories.TV_REVIEWS)
    main_category_for_subcategory3 = ITunesCategory(
        name=ITunesCategories.TV_AND_FILM, subcategories=[subcategory1, subcategory3]
    )

    category_list = format_category_list(subcategory1, subcategory3)
    assert category_list == [main_category_for_subcategory3]

    # The same subcategory twice
    category_list = format_category_list(subcategory1, subcategory1)
    assert category_list == [main_category_for_subcategory1]

    # One category and one subcategory from a different category
    category_list = format_category_list(category1, subcategory1)
    assert category_list == [category1, main_category_for_subcategory1]

    # One category and one subcategory from the same category
    category_list = format_category_list(
        ITunesCategory(name=ITunesCategories.TV_AND_FILM), subcategory1
    )
    assert category_list == [main_category_for_subcategory1]
