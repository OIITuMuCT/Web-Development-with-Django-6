# Django's database CRUD operations
`Creating operations`
1. [Creating an entry in the bookr database](#creating-an-entry-in-the-bookr-database)
2. [Using the `create()` method to create an entry](#using-the-create-method-to-create-an-entry)
3. Creating records for a `many-to-many` relationship
    1. [Creating records for a `many-to-one` relationship](#creating-records-for-a-many-to-one-relationship)
    2. [Creating records with `many-to-many` relationships](#creating-records-with-many-to-many-relationships)
    3. [A `many-to-many` relationship using the `add()` method](#a-many-to-many-relationship-using-the-add-method)
    4. [Using the `create()` and `set()` methods for `many-to-many` relationships](#using-the-create-and-set-methods-for-many-to-many-relationships)
4. [Create multiple records using `bulk_create`](#create-multiple-records-using-bulk_create)


`Read operations`
1. [Using the `get()` method to retrieve an object](#using-the-get-method-to-retrieve-an-object)
2. [Returning an object using the `get()` method](#returning-an-object-using-the-get-method)
3. [Using the `all()` method to retrieve a set of objects](#using-the-all-method-to-retrieve-a-set-of-objects)
4. [Using the `filter()` method to retrieve objects](#using-the-filter-method-to-retrieve-objects)
5. [Filtering by field lookups](#filtering-by-field-lookups)
6. [Using pattern matching for filtering operations](#using-pattern-matching-for-filtering-operations)

`Update operations`
1. [Using the `update()` method](#using-the-update-method)
2. [Update multiple records using bulk_update](#update-multiple-records-using-bulk_update)
`Delete operations`
1. [### Using the `delete()` method](#using-the-delete-method)



* ### Creating an entry in the bookr database
    <!-- Создание записи в базе данных bookr -->
    1. First, import the ModelName class/model from myapp.models:
        ```python
            from reviews.models import Publisher
        ```

    2. Create an object or an instance of the Published class by passing all the field values
    (name, website, and email) required by the Publisher model:
        ```python
        >>> publisher = Publisher(name='Packt Publishing',
            website='https://www.packtpub.com',
            email = 'info@packtpub.com)
        ```

    3. To call the `save()` method
        ```shell
        >>> publisher.save()
        ```
    
    4. Use the object attributes to make any further changes to the object and save the changes to the database:
        ```
        >>> publisher.email = 'info@packtpub.com'
        >>> publisher.email = 'customersupport@packtpub.com'
        >>> publisher.save()
        ```

* ### Using the `create()` method to create an entry
    1. First, import the Contributor class as before:
        ```python
            from reviews.models import Contributor
        ```

    2. Invoke the `create()` method to create an object in the database in a single step. Ensure that you pass all the required parameters (first_names, last_names, and email):
        ```python shell
        contributor = Contributor.objects.create(
            first_names="Rowel", last_names="Atienza",
            email="RowelAtienza@example.com"
        )
        ```

* ### Creating records for a `many-to-one` relationship
    1. First, import the Publisher class:
        ```python
            from reviews.models import Book, Publisher
        ```
    2. Retrieve the publisher object from the database using the following command. The get() method is used to retrieve an object from the database. `read/retrieve`
    ```python shell
        publisher = Publisher.objects.get(
            name='Packt Publishing'
        )
    ```
    3. When creating a book, we need to supply a date object, as publication_date is a date field in the Book model.
        ``` python shell
        from datetime import date
        ```
    4. Use the `create()` method to create a record of the book in the database.
        ```python shell
            book = Book.objects.create(
                title, "Advanced Deep Learning with Keras",
                publication_date=date(2018, 10, 31),
                isbn="9781788629416",
                publisher=publisher
            )
        ```

* ### Creating records with `many-to-many` relationships
    1. In case you have restarted the shell and lost the publisher and book objects
        ```python shell
            from reviews.models import Book
            from reviews.models import Contributor
            contributor = Contributor.objects.get(
                first_names='Rowel'
            )
            book = Book.objects.get(
                title='Advanced Deep Learning with Keras'
            )
        ```

    2. The way to establish a `many-to-many` relationship is by storing the information about
the relationship in the intermediary model or the relationship model; in this case, `BookContributor`.

        ```python
            from review.models import BookContributor
            book_contributor = BookContributor(
                book=book, 
                contributor=contributor, 
                role='AUTHOR'
            )
            book_contributor.save()
        ```

* ### A `many-to-many` relationship using the `add()` method
    1. If you have restart the shell, run the following two commands to import and fetch the desired book instance:

        ```python shell
            from reviews.models import Book, Contributor
            book = Book.objects.get(
                title="Advanced Deep Learning with Keras"
            )
        ```
    2. Use the `create()` method to create a contributor, as shown here:
        ```python shell
            contributor = Contributor.objects.create(
                first_names='Packt',
                last_names='Example Editor',
                email='PacktEditor@example.com'
            )
        ```
    3. Add the newly created contributor to the book using the `add()` method.
        ```python shell
            book.contributors.add(contributor, through_defaults={'role': 'EDITOR'})
        ```

* ### Using the `create()` and `set()` methods for `many-to-many` relationships
    ```python shell
        book.contributors.create(first_names='Packtp',
        last_names='Editor Example',
        email='PacktEditor2@example.com',
        through_defaults={'role': 'EDITOR'})

        from reviews.models import Publisher

        publisher = Publisher.objects.create(
            name='Pocket Books',
            website='https://pocketbookssampleurl.com',
            email='pocketbook@example.com'
        )

        contributor1 = Contributor.objects.create(
            first_names='Stephen', last_names='Stephen',
            email='StephenKing@example.com'
        )

        contributor2 = Contributor.objects.create(
            first_names='Peter', last_names='Straub',
            email='PeterStraub@example.com'
        )

        book = Book.objects.create(title='The Talisman',
        publication_date=date(2012, 9, 25),
        isbn='9781451697216', publisher=publisher)

        book.contributors.set([contributor1, contributor2],
            through_defaults={'role': 'CO_AUTHOR'})
    ```

* ### Using the `get()` method to retrieve an object
    1. Fetch a Publisher object that has a name field with the Pocket Books value:
        ```python shell
            from reviews.models import Publisher
            publisher = Publisher.objects.get(
                name='Pocket Books'
            )
        ```
    2. Re-enter the retrieved publisher object and press Enter:
        ```python shell
            >>> publisher
            <Publisher: Pocket Books>
        ```
    3. Upon retrieving the object, we have access to all the object's attributes(name, website, email).
        ```python shell
            >>> publisher.name
            'Pocket Books'

            >>> publisher.website
            'https://pocketbookssampleurl.com'
            # The publisher's email address can be retrieved as follows:
            >>> publisher.email
            'pocketbook@example.com'
        ```

* ### Returning an object using the `get()` method
    ```python shell
        >>> publisher = Publisher.objects.get(
            website='https://pocketbookssampleurl.com'
        )

        >>> publisher.name
        'Pocket Books'

        >>> Publisher.objects.get(pk=2)
        <Publisher: Pocket Books>
    ```

* ### Using the `all()` method to retrieve a set of objects
    ```python shell
        from reviews.models import Contributor

        >>> Contributor.objects.all()
        <QuerySet [<Contributor: Rowel>, <Contributor: Packt>, <Contributor: Packtp>,
        <Contributor: Stephen>, <Contributor: Peter>]>
    ```
    We can use list indexing to look up a specific object or to iterate over the list using an loop to do any other operation:

    ```python shell
        >>> contributors = Contributor.objects.all()

        >>> contributors[0]
        <Contributor: Rowel>

        >>> contributor[0].first_names
        'Rowel'
        >>> contributor[0].last_names
        'Atienza'
    ```

* ### Using the `filter()` method to retrieve objects
    1. First, create two more contributors:
        ```python shell
            from reviews.models import Contributor
            >>> Contributor.objects.create(first_names='Peter', 
            last_names='Wharton',
            email='PeterWharton@example.com')

            Contributor.objects.create(first_names='Peter',
            last_names='Tyrrell',
            email='PeterTyrrell@example.com')
        ```
    2. To retrieve those contributors who have a first_names value of Peter, and following code:
        ```python shell
            >>> Contributor.objects.filter(first_names='Peter')
            <QuerySet [<Contributor: Peter>, <Contributor: Peter>,
            <Contributor: Peter>]>
        ```
    3. The `filter()` method returns the object even if there is only one.
        ```python shell
            Contributor.objects.filter(first_name='Rowel')
            <QuerySet [<Contributor: Rowel>]>
        ```

    4. Furthermore, the `filter()` method returns an empty QuerySet if none matches the
query.

        ```python shell
            Contributor.objects.filter(first_name='Nobody')
            <QuerySet []>
        ```

* ### Filtering by field lookups
    ```python shell
        from reviews.models import Book
        book = Book.objects.filter(
            publication_date__gt=date(2014, 1, 1)
        )
        # __gt: Greater than
        # __lt: Less than
        # __lte: Less than or equal to
        # __gte: Greater than or equal to
    ```

* ### Using pattern matching for filtering operations
    ```python shell
    >>> book = Book.objects.filter(
        title__contains='Deep learning'
    )

    >>> book
    <QuerySet [<Book: Advanced Deep Learning with Keras>]>

    >>> book[0].title
        'Advanced Deep Learning with Keras' 
    ```

* ### Using the update() method
    ```python shell
        >>> from reviews.models import Contributor
        >>> Contributor.objects.filter(
            last_names='Tyrrell').update(
            first_names='Mike')
        1
    ```

* ### Using the `delete()` method
    1. Fetch the object using the get method and use the `delete()` method
    ```python shell
        >>> from reviews.models import Contributor
        >>> Contributor.objects.get(
            last_names='Wharton').delete()
        (1, {'reviews.Contributor': 1}
    ```

* ### Create multiple records using `bulk_create`
    1 . Import the Publisher model if you have not already imported it into your Django shell:

        ```python shell
        from reviews.models import Publisher
        >>> Publisher.objects.bulk_create(
            [
                Publisher(
                    name="New Town Publisher",
                    website="www.newtown.example.com",
                    email="newtown@example.com"
                ),
                Publisher(
                    name="Byron Bay Press",
                    website="www.byronbay.example.org",
                    email="byronbay@example.org",
                ),
                Publisher(
                    name="Katoomba Publisher",
                    website="www.katoomba.example.net",
                    email="katoomba@example.net",
                )
            ]
        )
        [<Publisher: New Town Publisher>, <Publisher: Byron Bay Press>, <Publisher: Katoomba Publisher>]
        ```

* ### Update multiple records using `bulk_update`
    ```python shell
    from reviews.models import Publisher
    publishers = [
        Publisher.objects.get(name="New Town Publisher"),
        Publisher.objects.get(name="Byron Bay Priss")
    ]
    publishers[0].website = "nswpublisher@example.com"
    publishers[0].website = "nswpublisher@example.com"
    # Updating
    >>>Publisher.objects.bulk_update(publishers, ["website"])
    2
    ```
