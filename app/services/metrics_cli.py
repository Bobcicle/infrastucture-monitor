from pprint import pprint

from app.services.metrics_service import collect_metrics


def main():
    metrics = collect_metrics()

    pprint(metrics.model_dump())


if __name__ == "__main__":
    main()