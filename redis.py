import time
import random
import string
import matplotlib.pyplot as plt
import numpy as np
from upstash_redis import Redis

# Initialize Redis connection
redis = Redis(url="", token="")

# In-memory storage for comparison
in_memory_store = {}

def generate_random_data(size=1000):
    """Generate random key-value pairs for testing"""
    data = {}
    for i in range(size):
        key = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        value = ''.join(random.choices(string.ascii_letters + string.digits, k=50))
        data[key] = value
    return data

def benchmark_redis_operations(data, operation_type="set"):
    """Benchmark Redis operations"""
    start_time = time.time()
    
    if operation_type == "set":
        for key, value in data.items():
            redis.set(key, value)
    elif operation_type == "get":
        for key in data.keys():
            redis.get(key)
    
    end_time = time.time()
    return end_time - start_time

def benchmark_memory_operations(data, operation_type="set"):
    """Benchmark in-memory operations"""
    start_time = time.time()
    
    if operation_type == "set":
        for key, value in data.items():
            in_memory_store[key] = value
    elif operation_type == "get":
        for key in data.keys():
            _ = in_memory_store.get(key)
    
    end_time = time.time()
    return end_time - start_time

def run_speed_comparison():
    """Run comprehensive speed comparison test"""
    data_sizes = [100, 500, 1000, 2000, 5000]
    redis_set_times = []
    redis_get_times = []
    memory_set_times = []
    memory_get_times = []
    
    print("Running Redis vs In-Memory Speed Comparison...")
    print("=" * 50)
    
    for size in data_sizes:
        print(f"Testing with {size} operations...")
        
        # Generate test data
        test_data = generate_random_data(size)
        
        # Benchmark SET operations
        redis_set_time = benchmark_redis_operations(test_data, "set")
        memory_set_time = benchmark_memory_operations(test_data, "set")
        
        # Benchmark GET operations
        redis_get_time = benchmark_redis_operations(test_data, "get")
        memory_get_time = benchmark_memory_operations(test_data, "get")
        
        redis_set_times.append(redis_set_time)
        redis_get_times.append(redis_get_time)
        memory_set_times.append(memory_set_time)
        memory_get_times.append(memory_get_time)
        
        print(f"  SET - Redis: {redis_set_time:.4f}s, Memory: {memory_set_time:.4f}s")
        print(f"  GET - Redis: {redis_get_time:.4f}s, Memory: {memory_get_time:.4f}s")
        print()
    
    # Create visualizations
    create_performance_charts(data_sizes, redis_set_times, redis_get_times, 
                            memory_set_times, memory_get_times)
    
    return {
        'data_sizes': data_sizes,
        'redis_set': redis_set_times,
        'redis_get': redis_get_times,
        'memory_set': memory_set_times,
        'memory_get': memory_get_times
    }

def create_performance_charts(data_sizes, redis_set, redis_get, memory_set, memory_get):
    """Create comprehensive performance charts"""
    
    # Create figure with subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Redis vs In-Memory Performance Comparison', fontsize=16, fontweight='bold')
    
    # Chart 1: SET Operations Comparison
    ax1.plot(data_sizes, redis_set, 'b-o', label='Redis SET', linewidth=2, markersize=8)
    ax1.plot(data_sizes, memory_set, 'r-s', label='In-Memory SET', linewidth=2, markersize=8)
    ax1.set_xlabel('Number of Operations')
    ax1.set_ylabel('Time (seconds)')
    ax1.set_title('SET Operations Performance')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Chart 2: GET Operations Comparison
    ax2.plot(data_sizes, redis_get, 'b-o', label='Redis GET', linewidth=2, markersize=8)
    ax2.plot(data_sizes, memory_get, 'r-s', label='In-Memory GET', linewidth=2, markersize=8)
    ax2.set_xlabel('Number of Operations')
    ax2.set_ylabel('Time (seconds)')
    ax2.set_title('GET Operations Performance')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # Chart 3: Bar Chart Comparison
    x_pos = np.arange(len(data_sizes))
    width = 0.35
    
    ax3.bar(x_pos - width/2, redis_set, width, label='Redis SET', alpha=0.8, color='blue')
    ax3.bar(x_pos + width/2, memory_set, width, label='Memory SET', alpha=0.8, color='red')
    ax3.set_xlabel('Data Size')
    ax3.set_ylabel('Time (seconds)')
    ax3.set_title('SET Operations - Bar Comparison')
    ax3.set_xticks(x_pos)
    ax3.set_xticklabels(data_sizes)
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # Chart 4: Performance Ratio
    set_ratios = [r/m if m > 0 else 0 for r, m in zip(redis_set, memory_set)]
    get_ratios = [r/m if m > 0 else 0 for r, m in zip(redis_get, memory_get)]
    
    ax4.plot(data_sizes, set_ratios, 'g-o', label='SET Ratio (Redis/Memory)', linewidth=2, markersize=8)
    ax4.plot(data_sizes, get_ratios, 'm-s', label='GET Ratio (Redis/Memory)', linewidth=2, markersize=8)
    ax4.axhline(y=1, color='k', linestyle='--', alpha=0.5, label='Equal Performance')
    ax4.set_xlabel('Number of Operations')
    ax4.set_ylabel('Performance Ratio')
    ax4.set_title('Redis vs Memory Performance Ratio')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('redis_vs_memory_performance.png', dpi=300, bbox_inches='tight')
    plt.show()

def print_summary_statistics(results):
    """Print summary statistics"""
    print("\nSUMMARY STATISTICS")
    print("=" * 50)
    
    avg_redis_set = np.mean(results['redis_set'])
    avg_memory_set = np.mean(results['memory_set'])
    avg_redis_get = np.mean(results['redis_get'])
    avg_memory_get = np.mean(results['memory_get'])
    
    print(f"Average SET time - Redis: {avg_redis_set:.4f}s, Memory: {avg_memory_set:.4f}s")
    print(f"Average GET time - Redis: {avg_redis_get:.4f}s, Memory: {avg_memory_get:.4f}s")
    print(f"SET Speed Ratio (Redis/Memory): {avg_redis_set/avg_memory_set:.2f}x")
    print(f"GET Speed Ratio (Redis/Memory): {avg_redis_get/avg_memory_get:.2f}x")
    
    if avg_memory_set < avg_redis_set:
        print(f"In-memory SET operations are {avg_redis_set/avg_memory_set:.2f}x faster")
    else:
        print(f"Redis SET operations are {avg_memory_set/avg_redis_set:.2f}x faster")
    
    if avg_memory_get < avg_redis_get:
        print(f"In-memory GET operations are {avg_redis_get/avg_memory_get:.2f}x faster")
    else:
        print(f"Redis GET operations are {avg_memory_get/avg_redis_get:.2f}x faster")

# Run the comparison test
if __name__ == "__main__":
    results = run_speed_comparison()
    print_summary_statistics(results)
