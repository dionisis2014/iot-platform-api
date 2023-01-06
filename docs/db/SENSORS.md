# Sensors table
Information of `sensors` table

## Definition
Name | Type | Size | NULL | Increment | Key
--- | --- | --- | --- | --- | ---
`id` | Integer | | no | yes | Primary
`name` | String | 32 | yes | |
`online` | Boolean | | no | |
`type` | String | 32 | no | |
`value` | Float | 16 | yes | |
`user_id` | Integer | | no | no | Foreign

## Details

### `id`
The unique integer id used by the database for a sensor.

### `name`
The name used by the user for the sensor.

### `online`
The online status of the sensor.

### `type`
The string representing the type of the sensor.

### `value`
The latest value of the sensor's measurement.

### `user_id`
The id of the user who owns this sensor.
