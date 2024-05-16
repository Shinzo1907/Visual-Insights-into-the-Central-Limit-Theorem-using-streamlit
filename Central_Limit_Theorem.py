import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def generate_population(size):
    # Create a population with a normal distribution
    population = np.random.normal(loc=50, scale=10, size=size)
    return population

def calculate_sample_means(population, sample_size, num_samples):
    sample_means = []
    for _ in range(num_samples):
        sample = np.random.choice(population, size=sample_size, replace=False)
        sample_means.append(np.mean(sample))
    return sample_means

def main():
    st.title("Central Limit Theorem")
    
    st.sidebar.header("Parameters")
    population_size = st.sidebar.number_input("Population Size", min_value=100, max_value=100000, value=1000, step=100)
    sample_size = st.sidebar.number_input("Sample Size", min_value=10, max_value=population_size, value=30, step=5)
    num_samples = st.sidebar.number_input("Number of Samples", min_value=10, max_value=1000, value=100, step=10)
    
    if sample_size > population_size:
        st.sidebar.error("Sample size must be less than or equal to population size.")
        return
    
    st.write("""
        The Central Limit Theorem (CLT) states that the distribution of the sample means 
        approximates a normal distribution (Gaussian distribution), regardless of the population's distribution, 
        provided the sample size is sufficiently large (usually n > 30). This theorem is foundational in 
        statistics because it justifies the use of the normal distribution in many statistical procedures and 
        hypothesis tests.According to the central limit theorem,the mean of a sample of data will be closer to
        the mean of the overall population"
    """)
    
    st.header("Population Statistics")
    population = generate_population(population_size)
    population_mean = np.mean(population)
    population_std = np.std(population)
    
    st.write("Population Mean:", population_mean)
    st.write("Population Standard Deviation:", population_std)
    
    st.header("Sample Statistics")
    sample_means = calculate_sample_means(population, sample_size, num_samples)
    avg_of_sample_means = np.mean(sample_means)
    
    st.write("Mean of Sample Means:", avg_of_sample_means)
    
    st.header("Graphical Demonstration")

    # Plot combined histogram
    fig, ax = plt.subplots()
    ax.hist(population, bins=30, alpha=0.5, label='Population', color='blue', density=True)
    ax.hist(sample_means, bins=30, alpha=0.5, label='Sample Means', color='green', density=True)
    ax.axvline(population_mean, color='blue', linestyle='dashed', linewidth=1, label='Population Mean')
    ax.axvline(avg_of_sample_means, color='green', linestyle='dashed', linewidth=1, label='Mean of Sample Means')
    ax.set_title('Population Distribution and Sample Means Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    ax.legend()
    st.pyplot(fig)
    st.markdown("""
        <div style="background-color: #f9f9f9; padding: 15px; border-radius: 5px; margin-top: 20px;">
            <h3 style="color: #2c3e50;">Graphical Interpretation</h3>
            <p style="color: #2c3e50;">Here, the histogram of <span style="color: green;">sample means</span> demonstrates the convergence towards a normal distribution,
            centered around the <span style="color: blue;">population mean</span>. As the number of samples increases,
            the sample means distribution becomes more tightly clustered around the population mean,
            illustrating the essence of the Central Limit Theorem.</p>
        </div>
    """, unsafe_allow_html=True)
if __name__ == "__main__":
    main()
