Matching key values
```sql
| concat(fields=["key1", "key2"], as="combined_key")
| combined_key match {
  /(.*)\1/ => is_match := "Yes";
  * => is_match := "No";
}
```
![regex101 example of matching key values](/regex101_match.jpg?raw=true "Matching Keys")

Splitting values into a new feature (column)
```sql
createEvents(["{\"index\":[\"A\", \"B\", \"C\", \"D\", \"E\"]}", 
              "{\"index\":[\"F\", \"G\", \"H\", \"I\", \"J\"]}", 
              "{\"index\":[\"K\", \"L\", \"M\", \"N\", \"O\"]}", 
              "{\"index\":[\"P\", \"Q\", \"R\", \"S\", \"T\"]}", 
              "{\"index\":[\"U\", \"V\", \"W\", \"X\", \"Y\"]}"])
| parseJson()
| split(field="index", strip=true)
```
