[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/kkazushi-eng/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/kkazushi-eng/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# Nov 19, 2026 — Three Nuclear Powers, One Table

An entry for make.fun's [news-image-20261119](https://make.fun/bounty/news-image-20261119):
sum up the world's news of Thursday 19 November 2026 in one image.

## The image

A newspaper front page dated **THURSDAY, NOVEMBER 19, 2026**, headlined
**"THREE NUCLEAR POWERS, ONE TABLE IN SHENZHEN"**.

The centrepiece is the day's dominant story: on the sidelines of the APEC
summit in Shenzhen, US President Donald Trump, China's Xi Jinping and
Russia's Vladimir Putin hold the first-ever trilateral US–China–Russia
summit. The three leaders sit at one round table with a globe, under their
national flags. Nuclear arms control, the war in Ukraine and the conflict
with Iran are on the agenda; US officials said no agreement was expected,
so the page reports the meeting itself, not an invented deal.

Three panels along the bottom carry the day's other headline stories:

- **HORMUZ: 3 TANKERS ABLAZE** — Iran said three oil tankers caught fire
  after striking mines east of the Strait of Hormuz.
- **WORLD COURT RULES ON ROHINGYA** — the International Court of Justice
  in The Hague hands down its judgment on Myanmar's alleged genocide of
  the Rohingya.
- **VOYAGER 1: ONE LIGHT-DAY AWAY** — NASA's Voyager 1, launched in 1977,
  becomes the first human-made object one full light-day from Earth.

A ticker along the foot adds the EU's proposed 45-billion-euro loan for
Ukraine, the worldwide rollout of GTA VI, and the wave of US tech outages.

## How it runs

`python3 main.py` (Python 3.13, standard library only, no network) copies
the bundled `entry.png` to `/output/entry.png` (or to
`$MAKEFUN_OUTPUT_DIR` when that variable is set) and checks the copy is
complete. It is deterministic: two runs write identical bytes. The image
is a 1024×1024 PNG, well under the 1 MiB limit.

## License

MIT — see `LICENSE`.
