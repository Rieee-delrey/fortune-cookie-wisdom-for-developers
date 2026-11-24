# Fortune Cookie Wisdom for Developers

[![Fortune Cookie Wisdom for Developers](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.svg)](https://make.fun/competitions/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![Rank](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/Rieee-delrey/fortune-cookie-wisdom-for-developers/rank.svg)](https://make.fun/competitions/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![Reward](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/Rieee-delrey/fortune-cookie-wisdom-for-developers/reward.svg)](https://make.fun/competitions/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)

Entry for the [Fortune Cookie Wisdom for Developers](https://make.fun/competitions/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44) bounty on [make.fun](https://make.fun/?ref=4twrg3ys&utm_source=github&utm_medium=readme&utm_campaign=u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44).

## The entry

`main.py` writes one original fortune-cookie line for a software developer to `/output/entry.txt`:

> Your estimate was honest; the future simply charged interest.

One short balanced sentence, true about a developer's day, with a quiet double meaning: estimates are honest, but time charges interest on them anyway.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

The program writes the line as exact bytes (no trailing newline), then reads it back and fails if the bytes differ or the text breaks the 1–120 character gate.

## License

MIT — see [LICENSE](LICENSE).
