# `/api/users/<user_name>`

## Methods
- `GET`
- `POST`
- `DELETE`

### `GET`
Body: `None`

Return:
Key | Type | Content
--- | --- | ---
`name` | String |
`sensors` | List | ids of user's sensors

### `POST`
Body:
Key | Type | Optional
--- | --- | ---
`name` | String | no
`online` | Boolean | no
`type` | String | yes

Return: `None`

### `DELETE`
Body: `None`

Return: `None`
