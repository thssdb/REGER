# REGER

In our paper **REGER: Reordering Time Series Data for Regression Encoding in Apache IoTDB**, we show some examples and performance about regression encoding with reordering.

To enable reproductivity, we share all datasets, algorithms and codes in the repository of encoding-reorder, and this readme guides will help you reproduce the results of the experiment and figures in the paper.

## 1. Directory Structure

    ├── README.md           // Help Document
    
    ├── compression_ratio  // Results
    
    │    ├── p_float_vary_p   // Result
    
    │    ├── pack_size_float   // Result
    
    │    ├── regulr_float   // Result
    
    │    ├── sota_ratio   // Result
    
    ├── data_draw  // Data for drawing some figures
    
    ├── example  // Results
    
    │    ├── result_evaluation   // Example

    |         ├── example100     // Datasets of examples
    
    │    └── other .py // // Codes of drawing examples
    
    ├── figs  // Figures
    
    ├── iotdb_datasets_lists      // Datasets of all the experiments
    
    └── other .py       // codes of drawing results

## 2. Environment Requirement

- IoTDB: download from branch [GitHub - apache/iotdb at research/encoding-reorder](https://github.com/apache/iotdb/tree/research/encoding-reorder)
- python: 3.8+
- modules needed: seaborn 0.11.1+, numpy, pandas

## 3. Code Execution

- Get results of compression ratio

```
java  xxx.java
```

- The algorithm corresponding to the java code is as follows

| algorithms                         | java code                                                                        |
| ---------------------------------- |----------------------------------------------------------------------------------|
| REGER         | iotdb\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\RegerFloatTest.java    |
| REGER sorted by time order |iotdb\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\RegerTimeSortTest.java  |
| REGER sorted by value order |iotdb\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\RegerValueSortTest.java  |
| REGER sorted by partition order |iotdb\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\RegerPartitionSortTest.java  |
| REGER sorted by random order |iotdb\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\RegerRandomSortTest.java  |
| REGER with prune | iotdb\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\RegerPruneTest.java    |
| Varying p | iotdb\iotdb-core\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\REGERPFloatTest.java  |
| Memory test | iotdb\iotdb-core\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\REGERPMemoryTest.java  |
| Other encoding |iotdb\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\EncodeTest.java         |
| Time space cost |iotdb\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\REGERTimeSpaceCostTest.java        |
| Value space cost |iotdb\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\REGERValueSpaceCostTest.java         |
| Time space cost |iotdb\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\BeforeREGERTimeSpaceCostTest.java        |
| Value space cost |iotdb\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\BeforeREGERValueSpaceCostTest.java         |
| Time cost of each initial order|iotdb\tsfile\src\test\java\org\apache\iotdb\tsfile\encoding\REGERFloatEachTimeTest.java         |

- Get figures about xxx.py

```
python xxx.py
```

- The figures corresponding to the python code are as follows

| Figures   | python code                                                                     |
| --------- | ----------------------------------------------------------------------------- |
| Figure 1  | draw_example0_63.py                                                     |
| Figure 2  | draw_example2_5.py                                                            |
| Figure 3  |                                                              |
| Figure 4  | draw_example3_2.py                                                              |
| Figure 5  | draw_distribution.py                                                          |
| Figure 6  |                                                 |
| Figure 7  | draw_examplea2.py                                                          |
| Figure 8  |                                                           |
| Figure 9  | draw_dataall_value_subgraph.py                             |
| Figure 10 | avg_transform_draw.py<br/>draw_compression_ratio.py                          |
| Figure 11 | avg_transform_draw_time.py<br/>draw_time.py                   |
| Figure 12 | avg_transform_draw_time.py<br/>draw_time.py                   |
| Figure 13 | avg_float_block_size.py<br/>draw_block_size_float.py                |
| Figure 14 | avg_transform_draw_time.py<br/>draw_time.py     |
| Figure 15 | avg_transform_draw.py<br/>draw_compression_ratio.py       |
| Figure 16 | avg_transform_draw_time.py<br/>draw_time.py       |
| Figure 17 | avg_float_block_size.py<br/>draw_block_size_float.py       |

## 4. Summary

https://metaso.cn/s/5oAHkG4