# web-unit-converter

Unit converter website with backend made in Django framework. \
Website allows conversions in units of length, mass, and temperature. \
Made conversions are saved to the local database and are accessible through history section on the main page. \

<br>

> [!NOTE]
> If the website is to be hosted, the `ALLOWED_HOSTS` variable should be updated to match the domain. \
> The history section is actually a list of all conversions made on the website, as there are no user accounts.

## Setting up the Environment
1. Ensure Python 3.13+ is installed.
2. Create a virtual environment for the project in the project's root directory, for example, by navigating to the project's root with `cd` and running `py -m venv venv`.
3. Install dependencies from `requirements.txt`.
4. Create a `.env` file based on the `.env.example` file in the `./unit_converter_web/` directory.
5. Create your local `db.sqlite3` database in the `./unit_converter_web/` directory by simply creating that file.
6. Navigate your terminal to `./unit_converter_web/`.
7. Run `manage.py runserver` and open the browser on the provided host.

<br>

> [!NOTE]
> If the project is hosted on a domain, there's no need to follow the steps below.

## How to Use

On the top of the main page, there are 3 sections, each corresponding to a different unit measurement system. \
By entering any of these, you can input a value and select its unit. \
Next, you can specify another unit to which the entered value should be converted. \
You can see the history of your conversions on the main page by clicking on the "See History" section.

## License

This project is licensed under the MIT License.
See [LICENSE](./LICENSE) for more information.

## Credits

- Idea: [https://roadmap.sh/projects/unit-converter](https://roadmap.sh/projects/unit-converter)
