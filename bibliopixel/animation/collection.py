from .. project import aliases, project
from . import animation, runner


class Collection(animation.BaseAnimation):
    def __init__(self, layout, animations=None):
        def make_animation(a):
            if isinstance(a, str):
                desc = {'animation': a[0]}
            elif isinstance(a, dict):
                desc = a
            else:
                desc = {'animation': a[0], 'run': a[1]}
            desc = aliases.resolve(desc)
            return project.make_animation(layout=layout, **desc)

        super().__init__(layout)

        self.animations = [make_animation(i) for i in animations or []]
        self.index = 0
        self.internal_delay = 0  # never wait

    # overriding to handle all the animations
    def cleanup(self, clean_layout=True):
        for a in self.animations:
            a.cleanup()
        super().cleanup(clean_layout)

    def add_animation(self, anim, **kwds):
        # DEPRECATED.
        anim.set_runner(runner.Runner(**kwds))
        self.animations.append(anim)

    def pre_run(self):
        self.index = -1

    @property
    def current_animation(self):
        return self.animations[self.index]