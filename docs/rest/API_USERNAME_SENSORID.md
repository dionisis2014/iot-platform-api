# `/api/<user_name>/<sensor_id>`

## Methods
- `GET`
- `PATCH`
- `DELETE`

### `GET`
Body: `None`

Return:
Key | Type
--- | ---
`id` | Integer
`name` | String
`online` | Boolean
`type` | String
`value` | Float

### `PATCH`
Body:
Key | Type | Optional
--- | --- | ---
`name` | String | yes
`online` | Boolean | yes
`type` | String | no

Return: `None`

### `DELETE`
Body: `None`

Return: `None`