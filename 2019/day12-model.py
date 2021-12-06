# from dataclasses import dataclass, field
from typing import List, Generator, TypeVar
import pytest

@dataclass(frozen=True)
class Vector:
  x: int = 0
  y: int = 0
  z: int = 0

  def magnitude(self):
    return abs(self.x) + abs(self.y) + abs(self.z)

  def __add__(self, other):
    return Vector(self.x+other.x, self.y+other.y, self.z+other.z)


@dataclass(frozen=True)
class Moon:
  pos: Vector
  velocity: Vector = field(default_factory=Vector)


  def energy(self):
    return self.pos.magnitude() * self.velocity.magnitude()


def load(text):
  """
  Load multi-line `text` into a collection of Moons
  """
  def vector(line):
    parts = line.strip("<>").split(",")
    return Vector(*[int(p.strip()[2:]) for p in parts])

  return [Moon(pos=vector(line)) for line in text.strip().splitlines()]


def simulate(moons: List[Moon]) -> List[Moon]:
  """
  Simulate the motion of `moons`, returning a new collection of Moons
  """
  def compare_axis(x, y):
    if x < y: return 1
    elif x == y: return 0
    else: return -1

  def gravity_vector(a: Vector, b: Vector) -> Vector:
    return Vector(
      x = compare_axis(a.x, b.x),
      y = compare_axis(a.y, b.y),
      z = compare_axis(a.z, b.z)
    )

  def simulate_moon(m: Moon) -> Moon:
    gravity = Vector()
    for n in moons:
      gravity += gravity_vector(m.pos, n.pos)
    velocity = m.velocity + gravity
    return Moon(pos=m.pos + velocity, velocity=velocity)

  return [simulate_moon(m) for m in moons]


def simulate_seq(moons: List[Moon]) -> Generator[List[Moon], None, None]:
  """
  Generate a sequence of simulated states for `moons`
  """
  m = moons
  while True:
    m = simulate(m)
    yield m


T = TypeVar("T")
def after(n: int, seq: Generator[T, None, None]) -> T:
  """
  Get the `n`th value from `seq`
  """
  for x in range(n):
    r = next(seq)
  return r


def total_energy(moons: List[Moon]) -> int:
  return sum(m.energy() for m in moons)


def test_load():
  """
  Verify parsing text into Moons
  """
  r = load("""<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>""")
  assert len(r) == 4
  assert r[0] == Moon(pos=Vector(-1, 0, 2))
  assert r[1] == Moon(pos=Vector(2,-10,-7))
  assert r[2] == Moon(pos=Vector(4,-8,8))
  assert r[3] == Moon(pos=Vector(3,5,-1))


EXAMPLE_MOONS_1 = [
  Moon(pos=Vector(-1,  0, 2)),
  Moon(pos=Vector( 2,-10,-7)),
  Moon(pos=Vector( 4, -8, 8)),
  Moon(pos=Vector( 3,  5,-1))
]

EXAMPLE_MOONS_2 = [
  Moon(pos=Vector(-8,-10,  0)),
  Moon(pos=Vector( 5,  5, 10)),
  Moon(pos=Vector( 2, -7,  3)),
  Moon(pos=Vector( 9, -8, -3))
]

@pytest.mark.parametrize("moons,steps,expect", [
  (EXAMPLE_MOONS_1, 1, [
    Moon(pos=Vector(2,-1, 1), velocity=Vector( 3,-1,-1)),
    Moon(pos=Vector(3,-7,-4), velocity=Vector( 1, 3, 3)),
    Moon(pos=Vector(1,-7, 5), velocity=Vector(-3, 1,-3)),
    Moon(pos=Vector(2, 2, 0), velocity=Vector(-1,-3, 1))
  ]),
  (EXAMPLE_MOONS_1, 2, [
    Moon(pos=Vector(5,-3,-1), velocity=Vector( 3,-2,-2)),
    Moon(pos=Vector(1,-2, 2), velocity=Vector(-2, 5, 6)),
    Moon(pos=Vector(1,-4,-1), velocity=Vector( 0, 3,-6)),
    Moon(pos=Vector(1,-4, 2), velocity=Vector(-1,-6, 2))
  ]),
  (EXAMPLE_MOONS_1, 10, [
    Moon(pos=Vector(2, 1,-3), velocity=Vector(-3,-2, 1)),
    Moon(pos=Vector(1,-8, 0), velocity=Vector(-1, 1, 3)),
    Moon(pos=Vector(3,-6, 1), velocity=Vector( 3, 2,-3)),
    Moon(pos=Vector(2, 0, 4), velocity=Vector( 1,-1,-1))
  ])
])
def test_simulate_one_step(moons, steps, expect):
  """
  Verify moon simulation
  """
  assert after(steps, simulate_seq(moons)) == expect



@pytest.mark.parametrize("moons,steps,energy", [
  (EXAMPLE_MOONS_1, 10, 179),
  (EXAMPLE_MOONS_2, 100, 1940)
])
def test_energy(moons, steps, energy):
  final = after(steps, simulate_seq(moons))
  assert total_energy(final) == energy


def part1(moons):
  final = after(1000, simulate_seq(moons))
  print(f"Part 1 : {total_energy(final)}")


if __name__ == "__main__":
  with open("day12.txt", "rt") as f:
    moons = load(f.read())

def simulate_until_repeat(moons: List[Moon]) -> int:
  """
  Simulate `moons` until a repeated state is seen. Returns the
  number of simulation steps to get to that state
  """
  def gcd(x: int, y: int) -> int:
    return y if x == 0 else gcd(y % x, x)

  def loop_size_for_axis(moons: List[Moon], axis) -> int:
    def state(m: List[Moon]) -> str:
      return str(list(axis(x) for x in m))

    states = set(state(moons))
    for n, m in enumerate(simulate_seq(moons)):
      s = state(m)
      if s in states:
        return n
      states.add(s)

  def axis_x(m): return (m.pos.x, m.velocity.x)
  def axis_y(m): return (m.pos.y, m.velocity.y)
  def axis_z(m): return (m.pos.z, m.velocity.z)

  overall_loop = 1
  for a in [axis_x, axis_y, axis_z]:
    loop = loop_size_for_axis(moons, a)
    overall_loop = overall_loop * loop // gcd(loop, overall_loop)

  return overall_loop