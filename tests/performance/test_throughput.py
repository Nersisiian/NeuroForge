# tests/performance/test_throughput.py
import time
import grpc
import cortex_pb2
import cortex_pb2_grpc

def test_parse_intent():
    channel = grpc.insecure_channel('localhost:50051')
    stub = cortex_pb2_grpc.CortexStub(channel)
    start = time.time()
    for i in range(10):
        resp = stub.ParseIntent(cortex_pb2.IntentRequest(text="Открой отчет по продажам"))
        assert resp.confidence > 0.5
    elapsed = time.time() - start
    print(f"10 запросов обработаны за {elapsed:.2f} сек ({10/elapsed:.1f} req/s)")

if __name__ == '__main__':
    test_parse_intent()
