Feature: verify if books are added and deleted using Library API

    @Library
    Scenario: verify AddBook API Functionality
        Given the book details which needs to be added to Library
        When we execute the AddBook PostAPI method
        Then book details added successfully
        And staus code of response should be 200

    @Library
    Scenario Outline: verify AddBook API Functionality
        Given the book details with <isbn> and <aisle>
        When we execute the AddBook PostAPI method
        Then book details added successfully
            Examples: 
                |isbn | aisle |
                |tys  | 2345  |
                |tyss | 5432  |

