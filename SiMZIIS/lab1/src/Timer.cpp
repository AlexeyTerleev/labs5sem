//
// Created by alexey_t on 06/09/23.
//

#include <chrono>

namespace ch = std::chrono;

template <typename duration = ch::seconds, typename clock = ch::high_resolution_clock>
class Timer
{
    typename clock::time_point m_start, m_stop;

public:
    void start() { m_start = clock::now(); }
    const Timer& stop()  { m_stop = clock::now(); return *this; }

    typename clock::rep get_time() const
    {
        return ch::duration_cast<duration>(m_stop - m_start).count();
    }
};