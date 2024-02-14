from flask import Flask, render_template, Blueprint
import os

from src.blueprints import BLUEPRINTS


class BlueprintApp(Flask):
    def __init__(
        self,
        template_folder: str,
        static_url_path: str,
        blueprints: list[Blueprint],
        import_name: str = __name__,
    ) -> None:
        super().__init__(
            import_name=import_name,
            template_folder=template_folder,
            static_url_path=static_url_path,
        )
        for bp in blueprints:
            assert isinstance(bp, Blueprint)
            self.register_blueprint(bp)

app = BlueprintApp(
    import_name=__name__,
    template_folder="templates",
    static_url_path="/src/assets",
    blueprints=BLUEPRINTS,
)


if __name__ == "__main__":
    app.run()
