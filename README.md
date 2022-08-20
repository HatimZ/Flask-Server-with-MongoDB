# Notes-Application

This a backend server of a Web application that allows CRUD operations on a database. The database used is MongoDB.
Create and READ can be done through the browser, but delete and update should be done through POSTMAN. This is because the HTML code is not written to
execute these commands in the browser.


## API Reference

#### READ all registered Users

```http
  GET '/All-Users'
```

Returns a List of all the Registered Users in the MongoDb table.

#### CREATE data in the database (Registers User)

```http
  POST /sign-up
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `email `      | `string` | **Required**.valid email |
| `firstName `      | `string` | **Required**. User name |

The API saves user in a local MongoDb table. Passwords are not saved.
The user enters details through a form.

#### UPDATE a User based on the ID which will be given in URL

```http
  PATCH /update/<id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id `      | `integer` | **Required**. A valid ID  |
| `email `      | `string` | **Required**.valid email |
| `firstName `      | `string` | **Required**. User name |

Updates user info if ID is valid otherwise if not prints a response 
that "Nothing is updated".


#### DELETE a User based on the ID which will be given in URL

```http
  DELETE /delete/<id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id `      | `integer` | **Required**. A valid ID  |
| `email `      | `string` | **Required**.valid email |
| `firstName `      | `string` | **Required**. User name |

Deletes user info if ID is valid otherwise if not prints a response 
that "User not deleted".





