# Network Traffic Monitoring and Classification

This project uses a packet sniffer and a pre-trained BERT model to monitor and classify network traffic. It also includes a web-based dashboard for visualizing the network traffic data.

## Features

- Packet sniffer that captures and analyzes network traffic
- AI model that classifies network traffic into ALLOW, ALERT, or BLOCK categories
- Dashboard that displays network traffic data and statistics

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/yourrepository.git
```

Install the required packages:

```bash
pip install -r requirements.txt
```

### Usage

Run the main script to start the packet sniffer and AI prediction model (make sure to run as root or administrator):

```bash
python main.py
```

Run and Open the dashboard in a web browser:

```bash
streamlit run Dashboard_v2.py
```

### Libraries Used

- Hugging Face Transformers: For loading the pre-trained BERT model
- Streamlit: For creating the dashboard
- Pandas: For data manipulation
- csv: For reading and writing CSV files
- Matplotlib: For data visualization
- Pre-Trained AI Model: https://huggingface.co/rdpahalavan/bert-network-packet-flow-header-payload
- Packet Sniffer (I watched a tutorial on YouTube and modified it to suit my needs): https://www.youtube.com/playlist?list=PL6gx4Cwl9DGDdduy0IPDDHYnUx66Vc4ed
