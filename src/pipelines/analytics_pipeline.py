from src.ingestion.data_loader import DataLoader
from src.warehouse.warehouse_manager import WarehouseManager
from src.analytics.marketplace_metrics import MarketplaceMetrics
from src.analytics.anomaly_detection import AnomalyDetector

loader = DataLoader("data/marketplace_tasks.csv")

df = loader.load_dataset()

df = loader.clean_data(df)

warehouse = WarehouseManager()

warehouse.create_tables(df)

metrics_engine = MarketplaceMetrics(df)

metrics = metrics_engine.compute_metrics()

print("Marketplace Metrics")

print(metrics)

detector = AnomalyDetector(df)

anomalies = detector.detect_outliers()

print("Detected Anomalies")

print(anomalies)
