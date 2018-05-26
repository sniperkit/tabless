#!/usr/bin/env python

import random


LOREM = """Nullam eu ante vel est convallis dignissim Fusce suscipit wisi nec
facilisis facilisis est dui fermentum leo quis tempor ligula erat quis odio
Nunc porta vulputate tellus Nunc rutrum turpis sed pede Sed bibendum Aliquam
posuere Nunc aliquet augue nec adipiscing interdum lacus tellus malesuada
massa quis varius mi purus non odio Pellentesque condimentum magna ut
suscipit hendrerit ipsum augue ornare nulla non luctus diam neque sit amet
urna Curabitur vulputate vestibulum lorem Fusce sagittis libero non molestie
mollis magna orci ultrices dolor at vulputate neque nulla lacinia eros Sed
id ligula quis est convallis tempor Curabitur lacinia pulvinar nibh Nam a
sapien""".split()

MAXINT = 10000
NUMROWS = 1000000000


def random_string(num_words=2, source=LOREM):
    pos = random.randint(0, len(source) - num_words - 1)
    return " ".join(source[pos:pos+num_words])


def main(num_cols=10, num_rows=NUMROWS):
    types = [int, float, str]
    col_types = [random.choice(types) for _ in range(num_cols)]

    for i in range(num_rows):
        cells = [str(i)]
        for col_type in col_types:
            if col_type is int:
                cells.append(str(random.randint(0, MAXINT)))
            elif col_type is float:
                cells.append(f"{random.random():.5f}")
            elif col_type is str:
                cells.append(random_string())

        row = "\t".join(cells)
        print(row)


if __name__ == '__main__':
    main()