Matching key values
```sql
| concat(fields=["key1", "key2"], as="combined_key")
| combined_key match {
  /(.*)\1/ => is_match := "Yes";
  * => is_match := "No";
}
```
![regex101 example of matching key values](/regex101_match.jpg?raw=true "Matching Keys")
