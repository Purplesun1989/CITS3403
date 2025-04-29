# tue 29-04

## Working Notes
- Compressed and changed images in assets file
  - Used rest of time i had to familiarise myself with johen's code

### Commands from mr gpt 
- `lsof -i :<port>`
  - Check what process is using `<port>`

```bash
find . -type f \( -iname '*.jpg' -o -iname '*.jpeg' \) \
  -execdir magick mogrify -quality 80 -format webp "{}" \;
```
- Command to batch compress and turn all images (.jpg) into (.webp)

```bash 
find . -type f \( -iname '*.jpg' -o -iname '*.jpeg' \) -exec mv -t /path/to/destination {} +
```
- Command to move all files into a seperate directory before deletion
  - Didn't work, i edited it to work `find . -type f\( -name '*.jpg' -o -iname '*.jpeg' \) -exec mv {} ~/path/to/dest \;`
