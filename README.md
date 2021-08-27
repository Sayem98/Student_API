
# Student API

Simple api using Django Rest Framework.

## Authors

- [@Sayem98](https://github.com/Sayem98)

  
## Deployment

To deploy this project run

```bash
  python manage.py runserver
```

  
## Documentation

[Documentation](https://linktodocumentation)
Project has three branches. Each branch represents a way to implement api in DRF.
### Master
Here first function based api view been implemented then class based api view been implemented.

### GenericAPIView
Api has been implenemted with GenericAPIView and ModelMixins.

### ConcreteViewClass
Api has been implemented with ConcreteViewClass. 
## API Reference

#### Get all student

```http
  GET /studentapi/
```
Get all student from the table.

#### Get student

```http
  GET /studentapi/${id}
```
Get a single item by the id.
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required**. Id of item to fetch |

#### Create a new Student

```http
  POST /studentapi/
```
Creates a new student. 

#### Update student

```http
  PUT /studentapi/${id}
```
Update a single student by the id.
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required**. Id of item to fetch |


#### Update partial student

```http
  PATCH /studentapi/${id}
```
Update a single partial student by the id.
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required**. Id of item to fetch |


#### Delete Student

```http
  DELETE /studentapi/${id}
```
Delete a single student by the id.
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required**. Id of item to fetch |
