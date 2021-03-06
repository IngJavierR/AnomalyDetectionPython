
import numpy as np
import pandas as pd


file_name = 'part-000'
data = pd.read_csv('data/'+file_name+'.csv')
filtered_columns = ['timestamp',
       'Memory space usage : ((MXBean(java.lang:name=Code Cache,type=MemoryPool).Usage.committed / MXBean(java.lang:name=Code Cache,type=MemoryPool).Usage.max))',
       'Heap usage activity : (d/dx (MXBean(java.lang:type=Memory).HeapMemoryUsage.used))',
       'DB connection started : (incld/dx (MXBean(com.bea:Name=source09,Type=JDBCConnectionPoolRuntime).ConnectionsTotalCount))',
       'Connection delay : (MXBean(com.bea:Name=source06,Type=JDBCDataSourceRuntime).ConnectionDelayTime)',
       'Memory space activity : (d/dx ((MXBean(java.lang:name=PS Old Gen,type=MemoryPool).Usage.committed / MXBean(java.lang:name=PS Old Gen,type=MemoryPool).Usage.max)))',
       'Active connections : (MXBean(com.bea:Name=source08,Type=JDBCConnectionPoolRuntime).ActiveConnectionsCurrentCount)',
       'Rel. heap committed : ((MXBean(java.lang:type=Memory).HeapMemoryUsage.committed / MXBean(java.lang:type=Memory).HeapMemoryUsage.max))',
       'Rel. nonHeap usage : ((MXBean(java.lang:type=Memory).NonHeapMemoryUsage.used / MXBean(java.lang:type=Memory).NonHeapMemoryUsage.max))',
       'Reserve request activity : (incld/dx (MXBean(com.bea:Name=source08,Type=JDBCDataSourceRuntime).ReserveRequestCount))',
       'Reserve request activity : (incld/dx (MXBean(com.bea:Name=source10,Type=JDBCDataSourceRuntime).ReserveRequestCount))',
       'Memory space usage : ((MXBean(java.lang:name=PS Perm Gen,type=MemoryPool).Usage.committed / MXBean(java.lang:name=PS Perm Gen,type=MemoryPool).Usage.max))',
       'Physical mem activity : (d/dx (MXBean(java.lang:type=OperatingSystem).FreePhysicalMemorySize))',
       'Rel. unavailable connections : ((MXBean(com.bea:Name=source02,Type=JDBCConnectionPoolRuntime).NumUnavailable / MXBean(com.bea:Name=source02,Type=JDBCConnectionPoolRuntime).CurrCapacity))',
       'Rel. nonHeap committed : ((MXBean(java.lang:type=Memory).NonHeapMemoryUsage.committed / MXBean(java.lang:type=Memory).NonHeapMemoryUsage.max))',
       'Connection delay : (MXBean(com.bea:Name=source09,Type=JDBCDataSourceRuntime).ConnectionDelayTime)',
       'Class loading activity : (d/dx (MXBean(java.lang:type=ClassLoading).LoadedClassCount))',
       'Memory space usage : ((MXBean(java.lang:name=PS Survivor Space,type=MemoryPool).Usage.used / MXBean(java.lang:name=PS Survivor Space,type=MemoryPool).Usage.max))',
       'Thread User time : (MXBean(java.lang:type=Threading).CurrentThreadUserTime)',
       'Available db connection activity : (d/dx (MXBean(com.bea:Name=source09,Type=JDBCDataSourceRuntime).NumAvailable))',
       'Memory space usage : ((MXBean(java.lang:name=PS Old Gen,type=MemoryPool).Usage.used / MXBean(java.lang:name=PS Old Gen,type=MemoryPool).Usage.max))',
       'No data',
       'DB connection started : (incld/dx (MXBean(com.bea:Name=source08,Type=JDBCConnectionPoolRuntime).ConnectionsTotalCount))',
       'Daemon thread count : (MXBean(java.lang:type=Threading).DaemonThreadCount)',
       'Available db connection activity : (d/dx (MXBean(com.bea:Name=source06,Type=JDBCDataSourceRuntime).NumAvailable))',
       'Memory space usage : ((MXBean(java.lang:name=PS Eden Space,type=MemoryPool).Usage.used / MXBean(java.lang:name=PS Eden Space,type=MemoryPool).Usage.max))',
       'Prepared statement cache hit rate : ((MXBean(com.bea:Name=source09,Type=JDBCDataSourceRuntime).PrepStmtCacheHitCount / MXBean(com.bea:Name=source09,Type=JDBCDataSourceRuntime).PrepStmtCacheMissCount))',
       'Class unloading activity : (d/dx (MXBean(java.lang:type=ClassLoading).UnloadedClassCount))',
       'Successful wait for connection : (incld/dx (MXBean(com.bea:Name=source09,Type=JDBCDataSourceRuntime).WaitingForConnectionSuccessTotal))',
       'Available db connection activity : (d/dx (MXBean(com.bea:Name=source08,Type=JDBCConnectionPoolRuntime).NumAvailable))',
       'Rel. unavailable connections : ((MXBean(com.bea:Name=source06,Type=JDBCConnectionPoolRuntime).NumUnavailable / MXBean(com.bea:Name=source06,Type=JDBCConnectionPoolRuntime).CurrCapacity))',
       'Memory space usage : ((MXBean(java.lang:name=PS Survivor Space,type=MemoryPool).Usage.committed / MXBean(java.lang:name=PS Survivor Space,type=MemoryPool).Usage.max))',
       'Memory space activity : (d/dx ((MXBean(java.lang:name=Code Cache,type=MemoryPool).Usage.used / MXBean(java.lang:name=Code Cache,type=MemoryPool).Usage.max)))',
       'Objects to be finalized : (MXBean(java.lang:type=Memory).ObjectPendingFinalizationCount)',
       'Active connections : (MXBean(com.bea:Name=source10,Type=JDBCDataSourceRuntime).ActiveConnectionsCurrentCount)',
       'Available db connection activity : (d/dx (MXBean(com.bea:Name=source05,Type=JDBCConnectionPoolRuntime).NumAvailable))',
       'Heap committed activity : (d/dx (MXBean(java.lang:type=Memory).HeapMemoryUsage.committed))',
       'Active connections : (MXBean(com.bea:Name=source09,Type=JDBCDataSourceRuntime).ActiveConnectionsCurrentCount)',
       'Last GC duration : (MXBean(java.lang:name=PS Scavenge,type=GarbageCollector).LastGcInfo.duration)',
       'Reserve request activity : (incld/dx (MXBean(com.bea:Name=source09,Type=JDBCDataSourceRuntime).ReserveRequestCount))',
       'NonHeap usage activity : (d/dx (MXBean(java.lang:type=Memory).NonHeapMemoryUsage.used))',
       'Rel. unavailable connections : ((MXBean(com.bea:Name=source03,Type=JDBCDataSourceRuntime).NumUnavailable / MXBean(com.bea:Name=source03,Type=JDBCDataSourceRuntime).CurrCapacity))',
       'Memory space activity : (d/dx ((MXBean(java.lang:name=PS Survivor Space,type=MemoryPool).Usage.used / MXBean(java.lang:name=PS Survivor Space,type=MemoryPool).Usage.max)))',
       'Connection delay : (MXBean(com.bea:Name=source08,Type=JDBCConnectionPoolRuntime).ConnectionDelayTime)',
       'Rel. unavailable connections : ((MXBean(com.bea:Name=source08,Type=JDBCConnectionPoolRuntime).NumUnavailable / MXBean(com.bea:Name=source08,Type=JDBCConnectionPoolRuntime).CurrCapacity))',
       'NonHeap committed activity : (d/dx (MXBean(java.lang:type=Memory).NonHeapMemoryUsage.committed))',
       'Memory space activity : (d/dx ((MXBean(java.lang:name=PS Perm Gen,type=MemoryPool).Usage.used / MXBean(java.lang:name=PS Perm Gen,type=MemoryPool).Usage.max)))',
       'Rel. heap usage : ((MXBean(java.lang:type=Memory).HeapMemoryUsage.used / MXBean(java.lang:type=Memory).HeapMemoryUsage.max))',
       'Swap activity : (d/dx (MXBean(java.lang:type=OperatingSystem).FreeSwapSpaceSize))',
       'GC time : (incld/dx (MXBean(java.lang:name=PS MarkSweep,type=GarbageCollector).CollectionTime))',
       'GC activity : (incld/dx (MXBean(java.lang:name=PS MarkSweep,type=GarbageCollector).CollectionCount))',
       'Memory space activity : (d/dx ((MXBean(java.lang:name=Code Cache,type=MemoryPool).Usage.committed / MXBean(java.lang:name=Code Cache,type=MemoryPool).Usage.max)))',
       'Memory space activity : (d/dx ((MXBean(java.lang:name=PS Old Gen,type=MemoryPool).Usage.used / MXBean(java.lang:name=PS Old Gen,type=MemoryPool).Usage.max)))',
       'Memory space activity : (d/dx ((MXBean(java.lang:name=PS Eden Space,type=MemoryPool).Usage.used / MXBean(java.lang:name=PS Eden Space,type=MemoryPool).Usage.max)))',
       'Rel. unavailable connections : ((MXBean(com.bea:Name=source05,Type=JDBCDataSourceRuntime).NumUnavailable / MXBean(com.bea:Name=source05,Type=JDBCDataSourceRuntime).CurrCapacity))',
       'Memory space usage : ((MXBean(java.lang:name=PS Old Gen,type=MemoryPool).Usage.committed / MXBean(java.lang:name=PS Old Gen,type=MemoryPool).Usage.max))',
       'Memory space activity : (d/dx ((MXBean(java.lang:name=PS Survivor Space,type=MemoryPool).Usage.committed / MXBean(java.lang:name=PS Survivor Space,type=MemoryPool).Usage.max)))',
       'Rel. unavailable connections : ((MXBean(com.bea:Name=source09,Type=JDBCConnectionPoolRuntime).NumUnavailable / MXBean(com.bea:Name=source09,Type=JDBCConnectionPoolRuntime).CurrCapacity))',
       'Rel. open file descriptors : ((MXBean(java.lang:type=OperatingSystem).OpenFileDescriptorCount / MXBean(java.lang:type=OperatingSystem).MaxFileDescriptorCount))',
       'Last GC duration : (MXBean(java.lang:name=PS MarkSweep,type=GarbageCollector).LastGcInfo.duration)',
       'Memory space activity : (d/dx ((MXBean(java.lang:name=PS Eden Space,type=MemoryPool).Usage.committed / MXBean(java.lang:name=PS Eden Space,type=MemoryPool).Usage.max)))',
       'Process CPU : (\Process(java)\CPU)']
data = data[filtered_columns]
print(data.shape)
data.to_csv('data/test-'+file_name+'.csv')