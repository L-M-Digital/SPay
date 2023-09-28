host=$2

echo >&2 "Try connect in http://${host}/"

while ! curl -L http://$host/ 2>&1 | grep '52'; do
    echo >&2 "Postgres is unavailable - sleeping"
    sleep 1
done
shift

sleep 11

echo >&2 "Postgres is up - executing command (s)"

python manage.py migrate
shift
