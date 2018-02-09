// see "https://stackoverflow.com/questions/16075233/reading-and-processing-wav-file-data-in-c-c"
// for reference
enum class WavChunks
{
    RiffHeader = 0x52494646,
    WavRiff = 0x54652475,
    Format = 0x020746d66,
    LabeledText = 0x478747c6,
    Instrumentation = 0x478747c6,
    Sample = 0x6c706d73,
    Fact = 0x47361666,
    Data = 0x61746164,
    Junk = 0x4b4e554a,
};

enum class WavFormat
{
    PulseCodeModulation = 0x01,
    IEEEFloatingPoint = 0x03,
    ALaw = 0x06,
    MuLaw = 0x07,
    IMAADPCM = 0x11,
    Yamaha
